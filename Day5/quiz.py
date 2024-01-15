# 1) 뉴스기사를 가져와서 단어별로 찢어서 리스트화 시키고 오름차순 정렬하기

article = """ All eyes will be on Taiwan this Saturday as voters choose a new leader under the shadow of an increasingly assertive China that has spent the past eight years ramping up its threats toward the self-ruled island.

The world will be watching to see not only who wins the election, but how democratic Taiwan’s authoritarian neighbor will respond. There, Xi Jinping – China’s most powerful leader in a generation – has called Taiwan’s unification with the mainland “a historical inevitability,” to be achieved by force if necessary.

The last time Taiwan had a change of government – when the ruling Democratic Progressive Party (DPP) came to power in 2016 – Beijing cut off most communications with Taipei and significantly increased economic, diplomatic and military pressure on the island in the ensuing years, turning the Taiwan Strait into one of the world’s major geopolitical flash points.

China’s ruling Communist Party views Taiwan as part of its territory, despite having never controlled it. While successive Chinese Communist leaders have vowed to eventually achieve “reunification,” Xi has repeatedly said the Taiwan issue “should not be passed down generation after generation,” linking the mission to his mid-century goal of “national rejuvenation.”

“This election marks a change in leadership at a moment when cross-strait tensions are high, and preserving stability has become more of a challenge,” said Amanda Hsiao, senior China analyst for the International Crisis Group.

“A conflict involving Taiwan is unlikely in the near term. But if one were to break out, the ramifications would be globally felt,” Hsiao said. 

All three candidates are selling themselves as the best choice for avoiding that doomsday scenario, pledging to maintain peace and the status quo – which polls have consistently shown is what most people in Taiwan want.

But the three men hold very different visions for how to achieve that goal. They all cite the need to boost Taiwan’s defense capabilities to deter China’s aggression but disagree on their policy priorities, particularly how to deal with Beijing.

Current DPP Vice President Lai Ching-te emphasizes bolstering Taiwan’s ties with like-minded democratic partners, such as the United States and Japan, while maintaining his administration’s stance that Tawain is already a de facto sovereign nation – a view Beijing deems unacceptable.

Hou Yu-ih, from the main opposition party Kuomintang (KMT), places more weight on resuming dialogue and deescalating tension with China.

Ko Wen-je from the Taiwan People’s Party (TPP), meanwhile, has called for a more “pragmatic” approach to seek a “new way out in the US-China rivalry,” though he has been less clear about what that means in practice.

Beijing’s response may vary depending on the election results, but experts say tension could rise further down the road regardless of who takes office, as China’s “reunification” plan has become a nonstarter for the vast majority of Taiwan’s 24 million people.

In addition to the threat from Beijing, livelihood issues such as low wages, high property prices and Taiwan’s slowly growing economy are expected be key factors in how they vote.
"""

wordList = article.split()
wordList.sort()
print(wordList)



