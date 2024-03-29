from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_similar_ingredients(stock_cupboard, new_ingredients, similarity_threshold = 0.7):
    stock_comparison = {}
    for stock_item in stock_cupboard:
        similar_items = []
        for menu_item in new_ingredients:
            similarity = similar(stock_item, menu_item)
        if similarity > similarity_threshold:
            similar_items.append(menu_item)
        if similar_items:
            stock_comparison[stock_item] = similar_items
    return stock_comparison

# create dummy stock cupboard

stock_cupboard = ['For the pasta and sauce:', '1 tbsp olive oil', '1 brown onion, finely chopped', 
                  '2 cloves garlic, finely chopped (or 1 cube frozen garlic)', '1/2 tsp chilli flakes', 
                  '500g passata', '4 cubes of frozen spinach', '1/2 tsp salt', '250g dried pasta', 
                  '125g whole-milk ricotta cheese', '25g grated Parmesan cheese', '110g shredded mozzarella cheese', 
                  '1 box lasagne sheets', '1 large onion, chopped', '3 cloves garlic, crushed', '1 tsp. dried oregano', 
                  '2 cans tomatoes', '10 mushrooms', '2 peppers', '4 carrots', 
                  "x spinach, (can use frozen spinach that's been thawed and drained of excess liquid)", 
                  'x g cheddar (grated)', '500ml milk', '1/2 tsp. ground cinnamon', 'x parmesan', '350 g mozzarella (optional)', 
                  '280g/10oz cherry tomatoes on the vine', '1 tbsp olive oil', '1.2 tbsp balsamic vinegar', '500g/1.1 lb gnocchi', 
                  '3 tbsp butter', '2 cloves garlic', '90g/3.3oz spinach', '2 tbsp chopped basil', 
                  '1/4 tsp cracked black pepper plus more for serving', '1/4 tsp sea salt plus more for serving', 
                  '210g Mozzarella cheese', '25g/2 tbsp pine nuts', 'For the batter:', '100g plain flour', '2 eggs', 
                  '150ml semi-skimmed milk', 'For the toad:', '8 pork sausages (or swap in some veggie)', '1 onion, finely sliced', 
                  '1 tbsp vegetable oil', 'For the gravy:', '1 onion, finely sliced', '1 tbsp vegetable oil', '2 tsp plain flour', 
                  '2 tsp English mustard', '2 tsp Worcestershire sauce', '1 vegetable stock cube, made up to 300ml', 
                  '1 cauliflower - cut into florets ', 'Chicken breast (optional)', 'olive oil', 'sea salt', 'freshly cracked black pepper', 
                  '2 tbsp  soy sauce', '2 tbsp hoisin sauce', '2 tbsp red wine vinegar', '1 tbsp toasted sesame oil', '2 tsp brown sugar',
                  '2 tsp cornflour', '2 garlic cloves, minced', '2 tsp freshly grated ginger', '1 tsp chilli flakes', '50g peanuts, chopped', 
                  '4 spring onions, thinly sliced', 'jasmine rice, for serving', '320g pack ready-rolled puff pastry', '2 tsp milk', '1 leek', 
                  '1 large roasted beetroot', '4 tbsp soft cheese', '200g goat cheese', '16g Marmite', '50g agave nectar', '2 tsp cornflour', 
                  '30ml mirin', '560g tofu', '100g roasted peanuts', '60ml soy sauce']
