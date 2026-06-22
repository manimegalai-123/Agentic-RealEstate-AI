from langgraph.graph import StateGraph
from graph.state import PropertyState

from agents.classifier_agent import classification_agent
from agents.feature_agent import feature_agent
from agents.price_agent import price_agent
from agents.description_agent import description_agent
from agents.poster_agent import poster_agent

from agents.owner_verification_agent import owner_verification_agent
from agents.listing_agent import listing_agent
from agents.buyer_notification_agent import buyer_notification_agent

from agents.recommendation_agent import recommendation_agent
from agents.notification_agent import notification_agent

workflow = StateGraph(PropertyState)

workflow.add_node(
    "classification",
    classification_agent
)

workflow.add_node(
    "feature",
    feature_agent
)

workflow.add_node(
    "price",
    price_agent
)

workflow.add_node(
    "description",
    description_agent
)

workflow.set_entry_point("classification")

workflow.add_edge(
    "classification",
    "feature"
)

workflow.add_edge(
    "feature",
    "price"
)

workflow.add_edge(
    "price",
    "description"
)


workflow.add_node(
    "poster",
    poster_agent
)
workflow.add_edge(
    "description",
    "poster"
)
workflow.add_node(
    "owner_verification",
    owner_verification_agent
)

workflow.add_node(
    "listing",
    listing_agent
)

workflow.add_node(
    "buyer_notification",
    buyer_notification_agent
)
workflow.add_edge(
    "poster",
    "owner_verification"
)

workflow.add_edge(
    "owner_verification",
    "listing"
)

workflow.add_node(
    "recommendation",
    recommendation_agent
)

workflow.add_node(
    "notification",
    notification_agent
)

workflow.add_edge(
    "listing",
    "recommendation"
)

workflow.add_edge(
    "recommendation",
    "notification"
)

workflow.add_edge(
    "notification",
    "buyer_notification"
)

workflow.set_finish_point(
    "buyer_notification"
)
app_graph = workflow.compile()