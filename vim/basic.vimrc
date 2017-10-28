" enable syntax highlighting
syntax enable

" show line numbers
" set number

" set tabs to have 2 spaces
set ts=2

" indent when moving to the next line while writing code
" set autoindent

" expand tabs into spaces
set expandtab

" when using the >> or << commands, shift lines by 4 spaces
set shiftwidth=4

" show a visual line under the cursor's current line
set cursorline

" show the matching part of the pair for [] {} and ()
" set showmatch

" enable all Python syntax highlighting features
let python_highlight_all = 1

" enbles spell check https://www.linux.com/learn/using-spell-checking-vim
setlocal spell spelllang=en_us


" https://stackoverflow.com/questions/5169638/autocompletion-in-vim
filetype plugin on
au FileType php setl ofu=phpcomplete#CompletePHP
au FileType ruby,eruby setl ofu=rubycomplete#Complete
au FileType python setl ofu=pythoncomplete#Complete
au FileType html,xhtml setl ofu=htmlcomplete#CompleteTags
au FileType c setl ofu=ccomplete#CompleteCpp
au FileType css setl ofu=csscomplete#CompleteCSS
