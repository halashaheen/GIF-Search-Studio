from dataclasses import dataclass

@dataclass
class GifItem:
    """Class to store and organize retrieved GIF data."""
    gif_id: str
    title: str
    rating: str
    url: str
    width: str
    height: str

    @classmethod
    def from_api_data(cls, item: dict) -> "GifItem":
        """Factory method to parse a single GIF object from the Giphy API."""
        original_image = item.get("images", {}).get("original", {})
        return cls(
            gif_id=item.get("id", "N/A"),
            title=item.get("title") or "Untitled GIF",
            rating=item.get("rating", "N/A").upper(),
            url=original_image.get("url", "No URL available"),
            width=original_image.get("width", "0"),
            height=original_image.get("height", "0"),
        )

    def display_summary(self, index: int) -> str:
        """Return a clean, formatted summary of the GIF."""
        return (
            f"GIF #{index}: {self.title}\n"
            f"  - ID         : {self.gif_id}\n"
            f"  - Rating     : {self.rating}\n"
            f"  - Dimensions : {self.width}x{self.height} px\n"
            f"  - Direct URL : {self.url}\n"
            f"{'-' * 50}"
        )