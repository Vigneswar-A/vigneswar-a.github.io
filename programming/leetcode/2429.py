class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.data = defaultdict(list)
        self.food_map = {}
        self.ratings = {}
        
        for food,cuisine,rating in zip(foods, cuisines, ratings):
            self.food_map[food] = cuisine
            self.ratings[food] = -rating
            heappush(self.data[cuisine], (-rating, food))
        

    def changeRating(self, food: str, newRating: int) -> None:
        heappush(self.data[self.food_map[food]], (-newRating, food))
        self.ratings[food] = -newRating
        

    def highestRated(self, cuisine: str) -> str:
        while self.data[cuisine]:
            rating, food = heappop(self.data[cuisine])
            if self.ratings[food] == rating:
                heappush(self.data[cuisine], (rating, food))
                return food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)