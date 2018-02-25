# Install this conf

ln -s diy/env-configs/scim/hidden.scimrc .scimrc

# Quick Cheat Sheet

NAVIGATE
hjkl

L, H lowest highest screen portions
g$, g0
gM - put me in da middle

TEXT NUMBERBLETS
>Text -> will write right aligned text
<Text -> will write text
\Text -> center text

= |  inserts number
aa | expand selected cell to fit text
fl, fh | increse, decrease collumnd width
fj, fk | increase, decrease decimal accuracy on col

e | edit a number cell
E | edit a text cell

dd | delete highlighted
dc | delete collumn
yr | copy row
pr | paste row
y | paste

9dr | delete 9 rows below


==========================

CALC

=@avg(X1:Y1) | calcs average

mod text

\"upper(X1:Y1)
\"upper("some feeeee")


# open csv with another delimiter


scim  EMP_LDAP_LT_NEW.csv --txtdelim=";"
