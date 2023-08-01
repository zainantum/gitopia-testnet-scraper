strCode=$(gitopiad query bank balances $GITOPIA_WALLET_ADDRESS | grep "amount" | sed 's/[^0-9]*//g')
strCode=$(($strCode*85/100))
gitopiad tx staking delegate $GITOPIA_VALOPER_ADDRESS "${strCode}utlore" --from=$WALLET --chain-id=$GITOPIA_CHAIN_ID --gas=auto
