msgs_list = ["There are no easter eggs here",
"I told you, no easter eggs",
"Zero... None.. why do you keep using this command",
"For real we dont have any easter eggs! stop!",
"You must be real bored right now, T_T ...",
"I will NOT give you an easter egg",
"Nope, i refuse",
"I said NO!",
"PLZ STAPH!",
"STAAAAPH!"
"Q_Q Fine you win , here you go",
"https://static.wikia.nocookie.net/egg-inc/images/2/28/Egg_easter.png/revision/latest/scale-to-width-down/256?cb=20190520212958",
"HAHA :D, Get Screwed! . I win n.n !",
"This command will self destruct now...",
"BOOOOM deleting command... DONE"
]

def get_easteregg(i):
  if (i>= 14):
    msg = "This command does nothing"
  else:
    msg = msgs_list[i]
  return msg