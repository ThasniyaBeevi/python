
def sort(dict1):

    for key in sorted(dict1):
        print("%s: %s" % (key, dict1[key]))
	

color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

sort(color_dict)