# GoldChain JSX Client

See [./tests](./tests) directory for documented tests that explain a lot of this client's functionality.

## TLDR

All methods have docstrings, _read_ them.

## Summary

1. [Client](#client): how to create, save and use a GoldChain client:
    1. [Create a Wallet](#create-a-wallet): how to create a GoldChain wallet (attached to a GoldChain client)
    2. [Unlockhash Get](#unlockhash-get): how to get information for addresses that do not belong to you
2. [Wallet](#wallet): how to save and use a GoldChain wallet:
    1. [Get address info](#get-address-info): Get (the) address(es) linked to this wallet
    1. [Check your balance](#check-your-balance)
    2. [Send Coins](#send-coins)
3. [Multi-Signature-Wallet](#multi-signature-wallet): learn how to view and manage Multi-Signature Wallets from your GoldChain wallet
5. [Atomic Swap Contacts](#atomic-swap-contracts): explains how to work with cross-chain atomic swaps, from a GoldChain perspective, using your GoldChain wallet
7. [Coin Minting](#coin-minting): a subsection devoted to the coin minters of the network
8. [Examples](#examples): examples that show how to use the GoldChain client as a library

### Client

Create a client as follows:

```python
c = j.clients.goldchain.new('my_client')
# available as `j.clients.goldchain.my_client` from now on
```

or

```python
# valid types: STD, TEST and DEV, by default it is set to STD
c = j.clients.goldchain.new('my_client', network_type='TEST')
# available as `j.clients.goldchain.my_client` from now on
```

The client is a JS config instance that can be saved.

#### Create a Wallet

```python
w = c.wallets.my_wallet.new("my_wallet") # a new seed will be generated
# available as `c.wallets.my_wallet` from now on
```

or:

```python
# wallet "recovery"
w = c.wallets.my_wallet.new("my_wallet", seed="carbon boss inject cover mountain fetch fiber fit tornado cloth wing dinosaur proof joy intact fabric thumb rebel borrow poet chair network expire else")
# available as `c.wallets.my_wallet` from now on
```

The wallet is a JS config instance that can be saved.

#### Other actions

Should you desire you can use the client
to get a block by height or ID (`c.block_get`), as well
as transactions by ID (`c.transaction_get`) and more.

Create a GoldChain client in Kosmos to explore all its options or check out
the [./tests](./tests) directory for documented tests.

##### Unlockhash Get

One can get all transactions and if applicable linked Multi-Signature Wallet addressed linked to a given Wallet Address
by using the `c.unlockhash_get` method:

```python
# the only parameter of `unlockhash_get` is as flexible as the recipient of the `w.coins_send` method (see for more info further in this doc)
result = c.unlockhash_get('01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214')
result.unlockhash # the unlockhash defined (or generated using the defined value)
result.transactions # a list of all transactions somehow linked to the given unlockhash (value)
result.multisig_addresses # a list of all Multi-Signature Wallet addresses linked to this wallet, only if applicable
```

From the result of `c.unlockhash_get` method one can compute the balance as follows:

```python
balance = result.balance() # human-readable printed in shell by default
# it does return however a very useful object
# should you want to inspect individual (coin) outputs
```

> Did you know that multiple balances can be merged?
> ```python
> balance = balance.balance_add(other_balance)
> ```

Finally, should it be desired, one can drain all available outputs of a balance object as follows:

```python
txns = balance.drain(recipient='01e64ddf014e030e612e7ad2d7f5297f7e74e31100bdf4d194ff23754b622e5f0083d4bedcc18d')
# a list of created transactions, empty if no outputs were available,
# each transaction will be filled as much as possible (taking into account the max coin inputs per transactions accepteable).
```

If unconfirmed avalable coin outputs should be drained with the confirmed coin outputs one can do so as follows:

```python
txns = balance.drain(recipient='01e64ddf014e030e612e7ad2d7f5297f7e74e31100bdf4d194ff23754b622e5f0083d4bedcc18d', unconfirmed=True)
# see the docs for the full info, but FYI: you can also attach optional data as well as an optional lock
```

Draining can for example be useful if you want to stop using a certain wallet and want to make
sure all outputs can be transferred are immediately transferred to your new wallet (`w.balance.drain`).
It can also be used to drain all available outputs of the Free-For-All Wallet (`c.unlockhash_get(None).balance()`).

### Wallet

#### Get address info:

```python
w.address            # the primary address (string)
w.addresses          # all individual addresses (list of strings, at least 1 element)
w.addresses_multisig # returns all known multisig addresses (list of strings, can be empty)
```

#### Check your balance:

```python
w.balance # human-readable printed in shell by default
# it does return however a very useful object
# should you want to inspect individual (coin) outputs
```

#### Send coins

To a single person:

```python
w.coins_send(
    recipient='01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214',
    amount=100)
# equivalent amount specifications:
#   - as a string: '100 gft', '100.0', '100.0 GFT', '100'
#   - as a Decimal: Decimal('100')
```

With a timelock:

```python
w.coins_send(
    recipient='01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214',
    amount='100 GFT',
    lock='01/02/2019 23:44:39') # can also be defined as an epoch timestamp: 1549064679
```

A timelock can also be defined by specifying a duration relative to now:

```python
w.coins_send(
    recipient='01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214',
    amount='200.30',
    lock='+7d') # you can use any of these 4 units, each 1 time: d (day), h (hours), m (minutes), s (seconds)
    # other, more full example: '+ 7d12h30m42s'
```

A timelock can also be defined by specifying a block height:

```python
w.coins_send(
    recipient='01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214',
    amount='10000',
    lock=42000) # will unlock at block height 42000
```

When sending coins you can also attach some data:

```python
w.coins_send(
    recipient='01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214',
    amount='100 RFT',
    data='this is some data') # can also be specified as bytes or bytearray for binary data
# optionally you can still attach a lock to it of course
```

To multiple people (a MultiSignature wallet), with the requirement that _all_ have to sign in order to spend it:

```python
w.coins_send(
    recipient=[
        '01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214',
        '01e64ddf014e030e612e7ad2d7f5297f7e74e31100bdf4d194ff23754b622e5f0083d4bedcc18d',
    ], amount='100.0')
# optionally you can still attach data and a lock to it of course
```

To multiple people (a MultiSignature wallet), with the requirement that some have to sign in order to spend it:

```python
w.coins_send(
    recipient=([
        '01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214',
        '01e64ddf014e030e612e7ad2d7f5297f7e74e31100bdf4d194ff23754b622e5f0083d4bedcc18d',
    ], 1), amount=100)
# signature count has to be at least 1,
# and cannot be greater than the amount of people you are sending to
# optionally you can still attach data and a lock to it of course
```

Optionally you can use the `refund` parameter to define the recipient of the refund, should a refund be required:

```python
(txn, submitted) = w.coins_send(
    recipient='01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214',
    amount=250,
    refund='01e64ddf014e030e612e7ad2d7f5297f7e74e31100bdf4d194ff23754b622e5f0083d4bedcc18d')
```

By default the primary wallet address will be used for refunds (`w.address`).
Refunds are required in case the sum of the defined amount and minimum transaction fee
is smaller than the sum value of the used coin inputs.

See [The Wallet Coins Send Unit Test](./tests/24_wallet_coins_send.py)
for detailed examples of sending coins to some address on the used GoldChain network.

### Multi-Signature Wallet

You use your regular wallet to manage and use your co-owned Multi-Signature wallets.

#### Check your balance:

The balance contains and reports the balance reports and outputs for all the Multi-Signatures
co-owned by your wallet as well.

```python
w.balance # human-readable printed in shell by default
# it does return however a very useful object
# should you want to inspect individual (coin) outputs
```

#### Send Coins

You send coins from your Multi-Signature wallet through your regular wallet,
by specifying the Multi-Signature wallet address of choice as the `source` parameter of your `coins_send` call:

```python
(txn, submitted) = w.coins_send(
    recipient='01f7e0686b2d38b3dee9295416857b06037a632ffe1d769153abcd522ab03d6a11b2a7d9383214',
    amount=10,
    source='039e16ed27b2dfa3a5bbb1fa2b5f240ba7ff694b34a52bfc5bed6d4c3b14b763c011d7503ccb3a',
# optionally you can still attach a lock and data,
# and the recipient is still as flexible as previously defined.
#
# specify the optional 'refund' parameter if you do not want it to refund to the
# 039e16ed27b2dfa3a5bbb1fa2b5f240ba7ff694b34a52bfc5bed6d4c3b14b763c011d7503ccb3a Multi-Signature Wallet,
# should a refund be required.
```

The `coins_send` call will return a pair `(txn, submitted)`, where the second value indicates if the value
was submitted. It is possible that there were not enough signatures collected, and that
other co-owners of you wallet still have to sign. If so you have to pass the returned transaction (`txn`) to them.

Using this client one can signs (and submit if possible)
a transaction using the `w.transaction_sign(txn)` method.

See [The Wallet Coins Send Unit Test](./tests/24_wallet_coins_send.py)
for detailed examples of sending coins to some address on the used GoldChain network
using a Multi-Signature wallet to fund and refund.

### Atomic Swap Contracts

Atomic swaps allow secure cross-chain transfers of money wihout any need of trust.
You an read more theory on Atomic Swaps as well as an example at <https://github.com/threefoldtech/rivine/blob/master/doc/atomicswap/atomicswap.md>.

Please ensure that you understand the terminlogy behind atomic swaps as otherwise the commands might make a lot of sense to you.

#### Commands

Create a contract as initiator:

```python
result = w.atomicswap.initiate(
    participator='0131cb8e9b5214096fd23c8d88795b2887fbc898aa37125a406fc4769a4f9b3c1dc423852868f6',
    amount=50, data='the beginning of it all') # data is optional, source and refund options are available as well
result.contract # the contract
result.transaction # contains the created (and if all good sent) transaction
result.submitted # if the contract was submitted (if not it is because more signatures are required)
result.secret # the random generated secret (Save it, but no yet share it)
```
> See [The AtomicSwap Initiate Unit Test](./tests/10_atomicswap_initiate.py) for a detailed example.

> Note: with atomic swap only unlock hashes (strings or `UnlockHash`) are supported, no Multi-Signature wallets can
> be the recipient or used for refunds.
> The refund is also used to identify the sender address of the Atomic Swap Contract.

Creating a contract as initiator without submitting it automatically to the network can be done as follows:

```python
result = w.atomicswap.initiate(
    participator='0131cb8e9b5214096fd23c8d88795b2887fbc898aa37125a406fc4769a4f9b3c1dc423852868f6',
    amount=50, submit=False) # submit=True by default, data, source and refund options are available as well
```

This is not common practise, but should you be in need of pre-submission (custom) validation,
you can do so by following the above approach.

Create a contract as participator:

```python
result = w.atomicswap.participate(
    initiator='01746b199781ea316a44183726f81e0734d93e7cefc18e9a913989821100aafa33e6eb7343fa8c',
    amount='50.0', secret_hash='4163d4b31a1708cd3bb95a0a8117417bdde69fd1132909f92a8ec1e3fe2ccdba') # data is optional, source and refund options are available as well
result.contract # the contract
result.transaction # contains the created (and if all good sent) transaction
result.submitted # if the contract was submitted (if not it is because more signatures are required)
```
> See [The AtomicSwap Participate Unit Test](./tests/11_atomicswap_participate.py) for a detailed example.

Creating a contract as participant without submitting it automtically to the network can be done as follows:

```python
result = w.atomicswap.participate(
    initiator='01746b199781ea316a44183726f81e0734d93e7cefc18e9a913989821100aafa33e6eb7343fa8c',
    amount='50.0', secret_hash='4163d4b31a1708cd3bb95a0a8117417bdde69fd1132909f92a8ec1e3fe2ccdba',
    submit=False) # submit=True by default, data is optional, source and refund options are available as well
```

This is not common practise, but should you be in need of pre-submission (custom) validation,
you can do so by following the above approach.

Verify a contract as recipient of an initiation contract:

```python
contract = w.atomicswap.verify('dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486',
    amount=50, secret_hash='e24b6b609b351a958982ba91de7624d3503f428620f5586fbea1f71807b545c1',
    min_refund_time='+1d12h', receiver=True)
# an exception is raised if the contract is not found, has already been spent
# or is not valid according to the defined information
```
> See [The AtomicSwap Verify-As-Receiver Unit Test](./tests/13_atomicswap_verify_receiver.py) for a detailed example.

Redeem a contract:

```python
transaction = w.atomicswap.redeem(
    'dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486',
    secret='f68d8b238c193bc6765b8e355c53e4f574a2c9da458e55d4402edca621e53756')
# an exception is raised when the contract is not found, has already been spent,
# or the wallet is not authorized as receiver.
```
> See [The AtomicSwap Redeem Unit Test](./tests/14_atomicswap_redeem.py) for a detailed example.

Refund a contract (only possible when the defined contract duration has expired):

```python
transaction = w.atomicswap.refund('a5e0159688d300ed7a8f2685829192d8dd1266ce6e82a0d04a3bbbb080de30d0')
# an exception is raised when the contract is not found, has already been spent,
# the defined secret is incorrect or the wallet is not authorized as sender.
```
> See [The AtomicSwap Refund Unit Test](./tests/15_atomicswap_refund.py) for a detailed example.

### Coin Minting

You can get the current minting condition active at the network as follows:

```python
condition = c.minter.condition_get()
condition.json       # the condition in JSON format
condition.unlockhash # the address of the wallet that is currently the minter
```

You can also get the current minting condition active at a given height in the network as follows:

```python
condition = c.minter.condition_get(height=1000)
condition.json       # the condition in JSON format
condition.unlockhash # the address of the wallet that is currently the minter
```

See [The Minter Condition Get Unit Test](./tests/25_minter_condition_get.py)
for detailed examples for getting the minter condition at a given height as
well as the latest minter condition for the used network.

Only if you have minting powers you can redefine the Mint Condition
(the condition to be fulfilled to proof you have these powers)
as well as create new coins. If you do have these powers, this subsection is for you.

Redefining the Mint Condition can be done as follows:

```python
(txn, submitted) = w.minter.definition_set(minter='01a006599af1155f43d687635e9680650003a6c506934996b90ae8d07648927414046f9f0e936')
# optional data can be attached as well,
# the minter parameter is as flexible as the recipient parameter when sending coins from your wallet.

# if not submitted yet, it's because you might require signatures from others:
# you can pass the txn in that case to the others, such that they can sign using:
(txn, signed, submitted) = w.transaction_sign(txn)
```

See [The Minter Condition Set Unit Test](./tests/26_minter_condition_set.py)
for detailed examples for setting a new minter condition.

Creating coins as a Coin Minter can be done as follows:

```python
(txn, submitted) = w.minter.coins_new(recipient='01a006599af1155f43d687635e9680650003a6c506934996b90ae8d07648927414046f9f0e936', amount=200)
# optional data can be attached as well,
# the recipient parameter is as flexible as the recipient parameter when sending coins from your wallet.

# if not submitted yet, it's because you might require signatures from others:
# you can pass the txn in that case to the others, such that they can sign using:
(txn, signed, submitted) = w.transaction_sign(txn)
```

See [The Minter Coins New Unit Test](./tests/27_minter_coins_new.py)
for detailed examples for minting new coins.

### Examples

The GoldChain Client is kept simple and focussed. It can do a lot, and it is very easy to use it.
However, that does mean that we do not support every possible use case out-of-the box.
Building an application on top of the GoldChain Client and as such using this client as a library.

#### Wallet Statements

You can find a detailed example in [The Wallet Statements Example](./tests/100_examples_wallet_statements.py)
on how to assemble your own statements for a wallet using the GoldChain Wallet Client.

The example is simple and prints the statements directly to the STDOUT as follows:

```
$ kosmos 'j.clients.goldchain.test(name="examples_wallet_statements")'
unconfirmed  Tx: 573290763024ae0a5e981412598a3d41bc02f8da628fa1e1adfe07d98818c689 |                          |         + 10 GFT         |
        > to: 0125c0156f6c1c0bc43c7d38e17f8948300564bef63caac05c08b0fd68996e494704bbbe0268cb
        > from: 01f0f397fd6b7b51b46ddd2ffda1e2240e639b19b47d27a4adc2bed78da0fc3d97c1fe7b972d1e
39997        Tx: 779cf13ecee7f45f032af92429056cd5976cb75ce968bab98e3e2fdf9a9b1034 |         - 1 GFT          |                          |
        > to: this wallet
        > from: this wallet
39995        Tx: b104308e683d4353a5a6b6cdfd4f6dfce39e241ff1218d6d6189bae89945034f |                          |        + 200 GFT         |
        > to: 0125c0156f6c1c0bc43c7d38e17f8948300564bef63caac05c08b0fd68996e494704bbbe0268cb
        > from: 015827a0cabfb4be5531ecd2b42470a25cf9910a868b857029c2bdabdc05cad51e66d5dd899064
39994        Tx: 208d9f524e937176e50a7399fd3886f584290948983bbd0ed781f59cefc343a8 |         - 11 GFT         |                          |
        > to: 01cb0aedd4098efd926195c2f7bba9323d919f99ecd95cf3626f0508f6be33f49bcae3dd62cca6
        > from: this wallet
39991        Tx: e7785bacd0d12f93ab435cf3e29301f15b84be82ae8abbdaed1cfd034f4ed652 |                          |        + 100 GFT         |
        > to: 0125c0156f6c1c0bc43c7d38e17f8948300564bef63caac05c08b0fd68996e494704bbbe0268cb
        > from: 01456d748fc44c753f63671cb384b8cb8a2aebb1d48b4e0be82c302d71c10f2448b2d8e3d164f6
39990        Tx: 544a204f0211e7642f508a7918c5d29334bd7d6892b2612e8acfb6dc36d39bd9 |                          |        + 400 GFT         |
        > to: 0125c0156f6c1c0bc43c7d38e17f8948300564bef63caac05c08b0fd68996e494704bbbe0268cb
        > from: 01773a1dd123347e1030f0822cb8d22082fe3f9b0ea8563d4ac8e7abc377eba920c47efb2fd736
