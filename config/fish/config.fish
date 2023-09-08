if status is-interactive

 set fish_greeting
 colorscript random 
 alias vim=nvim 
 export PATH="$HOME/.local/bin:$PATH"
 starship init fish | source 
	# Commands to run in interactive sessions can go here
end
