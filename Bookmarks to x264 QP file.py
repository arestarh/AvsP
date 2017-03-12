import codecs
import os.path

# run in thread
try:
    bookmarks = avsp.GetBookmarkList(title=False)
except TypeError:
    bookmarks = avsp.GetBookmarkList()
bookmarks.sort()
filename = avsp.GetSaveFilename(
                title=_('Save chapter file as...'), 
                default=os.path.splitext(
                    avsp.GetScriptFilename(propose='general', only='base'))[0],
                filefilter = '|'.join((_('QP files') + ' (*.qpf)|*.qpf',
                                       _('Text files') + ' (*.txt)|*.txt', 
                                       _('All files') + ' (*.*)|*.*')))
if not filename:
    return
text = []
for item in bookmarks:
       s = '%s K -1\n'% item
       text += [s]
       f = codecs.open(filename, 'w', 'utf-8')
       f.writelines(text)
       f.close()
