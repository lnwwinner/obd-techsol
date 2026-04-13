# Data Sources Module

class DataSources:
    def __init__(self):
        self.sources = {
            "trading": [
                "price_history",
                "technical_indicators",
                "order_book",
                "news_sentiment"
            ],
            "security": [
                "file_behavior",
                "api_calls",
                "network_activity"
            ],
            "general": [
                "user_input",
                "logs",
                "external_api"
            ]
        }

    def get_sources(self, domain):
        return self.sources.get(domain, [])
