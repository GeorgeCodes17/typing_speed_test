class tests:
    def test1(self):
        self.test_easy = "Aesop was one of the great Greek writers. He is best known for his"\
        ' fables, stories that have a moral. They teach us something about how we should '\
        'live our lives. Aesop wrote thousands of these stories. Here are a few. The Wolf'\
        " in Sheep's Clothing. Once upon a time, a Wolf decided to disguise the way he"\
        ' looked. He thought it would help him get food more easily. He put on the skin'\
        ' of a sheep, then he went out with the flock into the pasture. Even the shepherd'\
        ' was fooled by his clever disguise.'
        return self.test_easy
        # 96 words
    def test2(self):
        self.test_medium = 'Gold is a chemical element with the symbol Au and atomic number 79.'\
        ' It is a dense, soft, malleable and ductile metal with a bright yellow colour and '\
        'lustre, the properties of which remain without tarnishing when exposed to air or'\
        ' water. Chemically, gold is a transition metal and a group 11 element. It is one of'\
        ' the least reactive chemical elements, and is solid under standard conditions. As '\
        'the metallic native element mineral, gold structurally belongs to the isometric '\
        'copper group. Gold often occurs in free elemental form, as nuggets or grains, in '\
        'rocks, in veins, and in alluvial deposits. It occurs in a solid solutions series '\
        'with the native element silver, naturally alloyed with other metals like copper '\
        'and palladium and also as mineral inclusions.'
        return self.test_medium
        # 127 words
    def test3(self):
        self.test_hard = 'In both public and private organisations, we attempt to make decisions' \
        ' based on rigorous rational criteria, for example, by comparing costs and benefits'\
        ', using economic models, market surveys, commissioned scientific research, public'\
        ' opinion polling, and so on. This rational view of decision-making would have us '\
        'believe that when import issues are up for discussion we examine them logically'\
        ' and dispassionately - that the disagreements which occur in the course of our'\
        ' executive committee meeting arise from rational differences of opinion over, say'\
        ', the technical aspects of an investment decision or organisational restructuring'\
        '. Personal experience and empirical evidence do not support that view. Instead'\
        ' the evidence currently at hand would suggest the opposite, that disagreements '\
        'that arise in our executive committee meetings are often irrational in nature'\
        ' and do not in fact pertain to rational differences of opinion.'
        return self.test_hard
        # 137 words

tests = tests()

'''e = tests.test1().split()
m = tests.test2().split()
h = tests.test3().split()

count = 0
for items in m:
    count += 1

print(str(count) + ' words')'''
