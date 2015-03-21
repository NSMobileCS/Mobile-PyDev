import os

target='/sdcard/Pictures/nsfw'
# target should be the folder w/the
#images you want to be able to hide

manual=""" this script 'hides' any photos
or videos in a particular folder
(/sdcard/Pictures/nsfw by default)
so that Gallery doesn't show 
them. 

This is useful b/c otherwise gallery
shows all images on your sdcard,
including any objectionable photos.

1.Put your pics/vids in target folder
2.Run script 
3.at prompt, type hide to hide
or show to show
4.Run hide before letting coworkers
browse your photo gallery & you're safe


If you use a dif folder, just change 
the variable target (near top of file)
to match the directory you want to be 
able to hide and show again later.

It does the hiding by reversing the
file extensions, so a file called
myselfie.jpg -> myselfie.gpj
which gallery doesn't recognize

It does jpeg jpg png & mp4, easy to extend
if you need more formats

"""


 

def sho(target):
  os.chdir(target)
  exts={'gpj':'jpg', 'gepj':'jpeg', '4pm':'mp4', 'gnp':'png'}

  chlist=[]
  
  for fi in os.listdir('.'):
    s=fi.split('.')
    if s[-1] in exts:
      f=''.join(s[:-1])
      chlist.append((fi, f+'.'+exts[s[-1]]))
    
  print('chlist\n'+str(chlist))
  for s in chlist:
    #os.system("mv \"%s\" \"%s\"" % (target+'/'+s[0],	target+'/'+s[1]))
    #syscall="mv \"%s\" \"%s\"" % (target+'/'+s[0],	target+'/'+s[1])  	
    #print(syscall) 
    #uncomment the 2 lines above for debugging output

    print('showing %s.' % s[1])
    #comment above line to suppress showing files processed

  return 'ok.'

def hid(target):
  os.chdir(target)
  exts={'jpg':'gpj', 'jpeg':'gepj', 'mp4':'4mp', 'png':'gnp'}
  
  chlist=[]
  for fi in os.listdir('.'):
    s=fi.split('.')
    if s[-1] in exts:
      f=''.join(s[:-1])
      chlist.append((fi, f+'.'+exts[s[-1]]))
    
  
  for s in chlist:
    os.system("mv \"%s\" \"%s\"" % (target+'/'+s[0],	target+'/'+s[1]))    	
    print('hiding %s.' % s[0])
    #comment above line to suppress showing files processed

    #syscall="mv \"%s\" \"%s\"" % (target+'/'+s[0],	target+'/'+s[1])   	
    #print(syscall)  
    #uncomment the 2 lines above for debugging output
    
  return 'ok.'
  
  
  
if __name__ == '__main__':
  p=input('photoPriv: ')
  if p == 'show':
    sho(target)
  elif p=='hide':
    hid(target)
  elif p=='help':
    print(manual)
  else:
    print('warning: no action preformed')  
