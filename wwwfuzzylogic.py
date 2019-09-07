#zapier codes >>>
#company = ""
#recommend = ""
#output = {'Recommendation': recommend}


companies = [['Apple', 500, 7], ['Facebook', 600, -9], ['Amazon', 800, 17], ['Microsoft', 850, 12], ['Oracle', 900, -11], ['Google', 1000, 15], ['Salesforce', 1100, 14], ['Huawei', 1200, 1], ['Samsung', 1300, -2], ['Sony', 1400, -6], ['IBM', 1500, 12]]

scores = []
n = len(companies)
recommend = ""

companysales = 0.
companyprofit = 0.
companyscore = 0.

great_i = 0.
good_i = 0.
ok_i = 0.
risky_i = 0.
riskiest_i = 0.  #any company making a loss is not worth investing 

def checkloss(a):
  if a < 0:
    return 0.0
  return a

def checkave(a):
  if a < true_ave_score:
    return true_ave_score
  return a

#quick check of the position of the average score

for i in companies:
  if i[0] == company:
    companysales = float(i[1])
    companyprofit = float(i[2])
    companyscore = round(((i[2]/i[1])*100)**3, 3)  #assess performance based on profits earned from number of sales, and cubed to magnify significance

for j in companies:
  score = round(((j[2]/j[1])*100)**3, 3)
  scores.append(score)

ranked = sorted(scores, reverse = True)

toppercentile = int(round(n*0.1,0))
tp_score = ranked[toppercentile]
middlepercentile = int(round(n*0.3,0))
mp_score = ranked[middlepercentile]
lowerpercentile = int(round(n*0.9,0))
lp_score = ranked[lowerpercentile]


#removing the outliers top 90 percentile and below 10 percentile
true_sum = 0.
count = toppercentile
while count < lowerpercentile:
  true_sum = ranked[count] + true_sum 
  count += 1 
true_ave_score = true_sum / (lowerpercentile - toppercentile)

risky_i = checkloss(true_ave_score) 
ok_i = checkave(mp_score)
good_i = checkloss(ok_i)
great_i = checkloss(tp_score)

if companyscore < riskiest_i:
  recommend = "You don't want to invest in this firm, trust me"
if companyscore >= riskiest_i and companyscore < risky_i:
  recommend = "This firm is risky to invest in"
if companyscore >= risky_i and companyscore < good_i:
  recommend = "We are 50:50 on this"
if companyscore >= good_i and companyscore < great_i:
  recommend = "This is firm is safe to invest"
if companyscore >= great_i:
  recommend = "This is a great firm to invest in, put all your money in there"

#print(recommend)



#commented out the below for future descriptive statistical analysis

"""
sum_sales = 0.
sum_profit = 0.
ave_sales = 0.
ave_profit = 0.
max_sales = 0.
min_sales = 10000000000.
max_profit = 0.
min_profit = 10000000000.

for i in companies:
  sum_sales = sum_sales + i[1] 
  sum_profit = sum_profit + i[2]
  if i[1] >= max_sales:
    max_sales = i[1]
  if i[2] >= max_profit:
    max_profit = i[2]
  if i[1] <= min_sales:
    min_sales = i[1]
  if i[2] <= min_profit:
    min_profit = i[2]

ave_sales = sum_sales / len(companies)
ave_profit = sum_profit / len(companies)
ave_score = round((ave_profit/ave_sales*100)**3, 3)
"""

#print(ranked)
#print(sum_sales)
#print(sum_profit)
#print(ave_sales)
#print(ave_profit)
#print(max_sales)
#print(min_sales)
#print(max_profit)
#print(min_profit)
#print(highest_score)
#print(lowest_score)
#print(ave_score)
#highest_score = ranked[0]
#lowest_score = ranked[-1]
