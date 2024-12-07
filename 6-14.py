###
# Write a program that checks whether a given person is a
#  good influencer, that is, whether the person has at least two of
#  the following accounts: Facebook, Twitter or Instagram.
#  Use logical type variables: facebook, twitter, instagram,
#  the value of which indicates whether the person has an account
#  on the social networking site.
#

facebook = bool(int(input('Enter 1 (for yes) or 0 (for no) if you have a Facebook account: ')))
twitter = bool(int(input('Enter 1 (for yes) or 0 (for no) if you have a Twitter account: ')))
instagram = bool(int(input('Enter 1 (for yes) or 0 (for no) if you have a Instagram account: ')))


acc_num = sum([facebook, twitter, instagram])

if acc_num >= 2:
    print('You are a good influencer')
else:
    print('You are a terrible influencer')