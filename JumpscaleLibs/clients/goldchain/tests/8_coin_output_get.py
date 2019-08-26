from Jumpscale import j

from JumpscaleLibs.clients.blockchain.goldchain.stub.ExplorerClientStub import GoldChainExplorerGetClientStub


def main(self):
    """
    to run:

    kosmos 'j.clients.goldchain.test(name="coin_output_get")'
    """

    # create a goldchain client for devnet
    c = j.clients.goldchain.get("mytestclient", network_type="TEST")
    # or simply `c = j.goldchain.clients.mytestclient`, should the client already exist

    # (we replace internal client logic with custom logic as to ensure we can test without requiring an active network)
    explorer_client = GoldChainExplorerGetClientStub()
    # unspent coin output
    explorer_client.hash_add(
        "3b6543447cc0a0f9252382fbec2c933fa3031e20a1949246b6e45ba4b37aa863",
        '{"hashtype":"coinoutputid","block":{"minerpayoutids":null,"transactions":null,"rawblock":{"parentid":"0000000000000000000000000000000000000000000000000000000000000000","timestamp":0,"pobsindexes":{"BlockHeight":0,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":null,"transactions":null},"blockid":"0000000000000000000000000000000000000000000000000000000000000000","difficulty":"0","estimatedactivebs":"0","height":0,"maturitytimestamp":0,"target":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"totalcoins":"0","arbitrarydatatotalsize":0,"minerpayoutcount":0,"transactioncount":0,"coininputcount":0,"coinoutputcount":0,"blockstakeinputcount":0,"blockstakeoutputcount":0,"minerfeecount":0,"arbitrarydatacount":0},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":[{"id":"564a6d97b2d2f635ef26af90ab73268bbe7433c05d9f63a2f0b86615aabd4dc1","height":13506,"parent":"1ce5b4a280e05d577292184c0f823ea6b00ac1182614dd8db3ddf33609f94006","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"21609e91bc8dbe76a6dea0812b038bdb186ea55c60751aacb049fc91a01d7524","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"e851f6946aba8f29959fe747d308d99a825e1f3bcca791307e47a69ee0a71d160c0c27f0d79434dc4d47165448e3146ecfd3c837a96dfc1e052e27038c310507"}}}],"coinoutputs":[{"value":"1000000000","condition":{}},{"value":"1000840999999501","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}],"minerfees":["1000000000"],"arbitrarydata":"bW9yZSBmcmVlIG1vbmV5"}},"coininputoutputs":[{"value":"1000842999999501","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["3b6543447cc0a0f9252382fbec2c933fa3031e20a1949246b6e45ba4b37aa863","95fbf2ec69fcf867d2e75db5932c5a6a5f1ee4ec47a4063bfefa5cac8887c4d2"],"coinoutputunlockhashes":["","0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false}],"multisigaddresses":null,"unconfirmed":false}',
    )
    # spent coin output
    explorer_client.hash_add(
        "21609e91bc8dbe76a6dea0812b038bdb186ea55c60751aacb049fc91a01d7524",
        '{"hashtype":"coinoutputid","block":{"minerpayoutids":null,"transactions":null,"rawblock":{"parentid":"0000000000000000000000000000000000000000000000000000000000000000","timestamp":0,"pobsindexes":{"BlockHeight":0,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":null,"transactions":null},"blockid":"0000000000000000000000000000000000000000000000000000000000000000","difficulty":"0","estimatedactivebs":"0","height":0,"maturitytimestamp":0,"target":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"totalcoins":"0","arbitrarydatatotalsize":0,"minerpayoutcount":0,"transactioncount":0,"coininputcount":0,"coinoutputcount":0,"blockstakeinputcount":0,"blockstakeoutputcount":0,"minerfeecount":0,"arbitrarydatacount":0},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":[{"id":"564a6d97b2d2f635ef26af90ab73268bbe7433c05d9f63a2f0b86615aabd4dc1","height":13506,"parent":"1ce5b4a280e05d577292184c0f823ea6b00ac1182614dd8db3ddf33609f94006","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"21609e91bc8dbe76a6dea0812b038bdb186ea55c60751aacb049fc91a01d7524","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"e851f6946aba8f29959fe747d308d99a825e1f3bcca791307e47a69ee0a71d160c0c27f0d79434dc4d47165448e3146ecfd3c837a96dfc1e052e27038c310507"}}}],"coinoutputs":[{"value":"1000000000","condition":{}},{"value":"1000840999999501","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}],"minerfees":["1000000000"],"arbitrarydata":"bW9yZSBmcmVlIG1vbmV5"}},"coininputoutputs":[{"value":"1000842999999501","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}},"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}],"coinoutputids":["3b6543447cc0a0f9252382fbec2c933fa3031e20a1949246b6e45ba4b37aa863","95fbf2ec69fcf867d2e75db5932c5a6a5f1ee4ec47a4063bfefa5cac8887c4d2"],"coinoutputunlockhashes":["","0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"e6aba8ef554873e5a2bb8eea69821ebe50b821123756e5b125aaed7e3b16550b","height":13504,"parent":"e5bb01658c50a9b7f120f5a7abeb0d00297e552714c56a17d9f16afc0c7b133e","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"4be59838a2baaf69afbc558e961aae584f69b74ab72321799f380d02d5adea01","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"25d62e238f4bba70efe620e452108028453190e0d4a088943a2c43b7723c4740e6509284261bfb3f2d4b661e236ff9b3e0ad4eab4d11cd4476a9debb87829808"}}},{"parentid":"6eb896edab9539b41077a7fb540a4987d5e8b434ec77e150c1e571d2883652f2","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"c3b93315954a89e389021c036c7924f019875291b165894651780059144034747c780d7d22a6f8483afab8b3ccba0713152f45ad97ededbf3eb9d35b3102fd04"}}},{"parentid":"0ffc3aceee0f3f695d1173056998e49e964c72c6b9d9ce08258f51cce6d9cd18","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"d21c74746ba9e8e727c8c87fe3990637d1491c2aa038bd8884de687cff80c1f33e9af0fb08c95f3cd7d74752b1e10f159838ef6097c25bae395525a7eefe1e0c"}}},{"parentid":"170815e3fd93f34e5b40644dd116efcfa27fd3e4f6992a68759978336a16fe5e","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"5ae40bae07d7a1ffd4cef41fa611390bc9c151351853e735857cfd6238d9478b73d971f76d9c93061f6b2eea2e2ec30f4e96abb32e0408cfad00fa0a0b373f0b"}}},{"parentid":"445579891a0c84b3b362f5266204c7b34cebe50b9d55ea6c9a05048baf7b5bf2","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"421742cdaf1fb9f208cea23d73bfdf928102cec826086fce1dbbf86108d63bde992323d59ad82ce43d08f6c2a6d817ac007f1fcf00d318c51a8532da7a54f006"}}},{"parentid":"4f524b591aea65c5b36c8ef18102f2a69d6a7e07c54e3cedbd6fc85ac8ed2611","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"a495c13415bafdaac50376952a4c6e5ef0e35b24e49e5c32bc5a4d86bf25e0f9952b04153819d808ac19919e30f51c3822d73b050529a2dee04d027c32ab0005"}}},{"parentid":"ea75d01b64a05e1652bbc334a9fabf8ec0fa11f02c7d3657b4be3f3270a927d5","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"eb91f93e757d402fd50dce312315183760a5e2f82ae457006f60c45766c11d81ec9f217366b52b1a33762f657b736d3350046f6d307cf88788ef91107cfc5d0c"}}},{"parentid":"4834fadc322aa9cfdef0294e98624424c1f972523d335f8ae45175b1035f8958","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"907eb0f07af54ebc9d020acb344a15b4dabf2682c6c810ed3a9a745b795ec0a50cf73fb91c0bef04a69c3f81cb3a7ae121427d3a54891323e6ee07890f5ee806"}}},{"parentid":"ebd166582e892cdbbc01b71c29b9a0e64f0f69eb91e7a1d99ffde99307ecaa2e","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"6b5346e30bf439006ae8f8564832a7d1677bdedf7bda0bdf63f0a0df6949105b9626f3eab532e87ddddbb38871138844d76ac00821e300f2ff8a9a6a3c615c05"}}},{"parentid":"28bcc4bdef67f304b64b4525443c5257f775ea89122a6b9f2f4526af701aaeff","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"63024d6363369e56e5c4808a9fadcd1d8d5632cdc14b547b09ed8f280b1b8691315078b58b76ac1219f0425e60b941bf3f6f7d315bdef69dd9f0b91644c48c05"}}},{"parentid":"5cc1cdcd0962403ee112509033c87eca5e07468f3c996f1f1e3240a6e806a920","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"941ce8d3d4808bf455a2db092c1e11d5350649d9be5febaa5c00437260baf17e259ea853687e4692c3e9bd51502c3e3f3d524757ba0e44ff31599bad1ae6ef04"}}},{"parentid":"126e7a270a3548a67e7756497506a4a53e578d5b818d7dec28117f92f8b74a6d","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"2bc5e3de04e03a64369e93e69f191e2ffe3202e1cbcf174e86a99d8c3dbcd6f3332048c323a9b429b82e9a8df6ee22ba757631274fa7b96476c0dd5cc37ffa0d"}}},{"parentid":"5ff190d50ea0d63ecfdd1500aa146344864c82512e1492947405552e1689d31a","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"ec611cc4f11e0e7448e7a08357e5892ee02f05622aa4d45057b9f97167c1d6f3f310f8584a91c9e8bcdae9e2014ee69f69d8a8f4010fbbe13b46b0af39b88f0c"}}},{"parentid":"63891de50dcb285689e1cd02618917ab9df4c6001f14e63532a5a75716ec0b6c","fulfillment":{"type":1,"data":{"publickey":"ed25519:89ba466d80af1b453a435175dbba6da7718e9cb19c64c0ed41fca3e6982e3636","signature":"addf2585a4c2103ecd83cf7d6a77709ab1d8f132083ef8254c005aae38856bc5eb7143dd39bfca19ccd9a52e98532b3defedb11d529365c1d137912d0a35570a"}}}],"coinoutputs":[{"value":"1000842999999501","condition":{"type":1,"data":{"unlockhash":"0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"1","condition":{},"unlockhash":""},{"value":"1000000000","condition":{},"unlockhash":""},{"value":"1000000000","condition":{},"unlockhash":""},{"value":"42000000000","condition":{},"unlockhash":""},{"value":"89000000000","condition":{},"unlockhash":""},{"value":"1000000000","condition":{},"unlockhash":""},{"value":"100000000000","condition":{},"unlockhash":""},{"value":"1000000000","condition":{},"unlockhash":""},{"value":"1000000000","condition":{},"unlockhash":""},{"value":"475999999500","condition":{},"unlockhash":""},{"value":"1000000000000000","condition":{"type":3,"data":{"locktime":42,"condition":{}}},"unlockhash":""},{"value":"1000000000","condition":{},"unlockhash":""},{"value":"89000000000","condition":{},"unlockhash":""},{"value":"42000000000","condition":{},"unlockhash":""}],"coinoutputids":["21609e91bc8dbe76a6dea0812b038bdb186ea55c60751aacb049fc91a01d7524"],"coinoutputunlockhashes":["0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false}],"multisigaddresses":null,"unconfirmed":false}',
    )
    # spent block stake output
    explorer_client.hash_add(
        "fb3644143770aeef28020b8bea7c35320cb1e2341d17a338389bd7e3afb9990b",
        '{"hashtype":"blockstakeoutputid","block":{"minerpayoutids":null,"transactions":null,"rawblock":{"parentid":"0000000000000000000000000000000000000000000000000000000000000000","timestamp":0,"pobsindexes":{"BlockHeight":0,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":null,"transactions":null},"blockid":"0000000000000000000000000000000000000000000000000000000000000000","difficulty":"0","estimatedactivebs":"0","height":0,"maturitytimestamp":0,"target":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"totalcoins":"0","arbitrarydatatotalsize":0,"minerpayoutcount":0,"transactioncount":0,"coininputcount":0,"coinoutputcount":0,"blockstakeinputcount":0,"blockstakeoutputcount":0,"minerfeecount":0,"arbitrarydatacount":0},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":[{"id":"a277de3f98a75e3199b1829b4f71093b23044e0fc995cb98224fe22ebda14c84","height":14733,"parent":"62d947526f5012d771c9618851fbf7069930a9106c53cd89dda858738b84f6f1","rawtransaction":{"version":1,"data":{"coininputs":null,"blockstakeinputs":[{"parentid":"a877078376f423d4f7a477959adffdaa58e445f39ef00c94330d7bf89a053535","fulfillment":{"type":1,"data":{"publickey":"ed25519:d285f92d6d449d9abb27f4c6cf82713cec0696d62b8c123f1627e054dc6d7780","signature":"b52b1aedb4e228914356490467cfcdae4d09d68c214806b358e8e503232fd9d5865ff14ed9196154343498001a25c17396e2109015f21c67387c9a5ea9490706"}}}],"blockstakeoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}}}],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}},"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}],"blockstakeoutputids":["fb3644143770aeef28020b8bea7c35320cb1e2341d17a338389bd7e3afb9990b"],"blockstakeunlockhashes":["015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"],"unconfirmed":false},{"id":"ba0be0145a3415440eddf5cf6f5268e3119c4ab67207652efb6783f0723b0aba","height":14734,"parent":"1f9454cef5a71e9b43ef2eae35bfb6171b596e96177d9a6ef59a9bd2ec854b30","rawtransaction":{"version":1,"data":{"coininputs":null,"blockstakeinputs":[{"parentid":"fb3644143770aeef28020b8bea7c35320cb1e2341d17a338389bd7e3afb9990b","fulfillment":{"type":1,"data":{"publickey":"ed25519:d285f92d6d449d9abb27f4c6cf82713cec0696d62b8c123f1627e054dc6d7780","signature":"7ea47daa3d131f9bb28a7b0aebc9c9399ba6d9f1ae216d85ff6a6735362f9fc4bca4c0ec3de2d5b386187d882f7b5f76e9846e5f6c559d3bb196dd38c6d46e0c"}}}],"blockstakeoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}}}],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}},"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}],"blockstakeoutputids":["cf9dc7e9bf57d2ad9be81fa9d1039f41e55afc743f7bce5e5379cf4d8a8ce018"],"blockstakeunlockhashes":["015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"],"unconfirmed":false}],"multisigaddresses":null,"unconfirmed":false}',
    )
    c._explorer_get = explorer_client.explorer_get

    # get an unspent coin output
    co, creation_txn, spend_txn = c.coin_output_get("3b6543447cc0a0f9252382fbec2c933fa3031e20a1949246b6e45ba4b37aa863")
    assert spend_txn is None
    assert co is not None
    assert creation_txn is not None
    assert co.id == "3b6543447cc0a0f9252382fbec2c933fa3031e20a1949246b6e45ba4b37aa863"
    assert str(co.value) == "1"
    assert (
        str(co.condition.unlockhash) == "000000000000000000000000000000000000000000000000000000000000000000000000000000"
    )
    assert len(creation_txn.coin_inputs) == 1
    assert (
        str(creation_txn.coin_inputs[0].parentid) == "21609e91bc8dbe76a6dea0812b038bdb186ea55c60751aacb049fc91a01d7524"
    )
    assert len(creation_txn.coin_outputs) == 2
    assert creation_txn.coin_outputs[0] == co
    assert creation_txn.coin_outputs[1].id == "95fbf2ec69fcf867d2e75db5932c5a6a5f1ee4ec47a4063bfefa5cac8887c4d2"
    assert (
        str(creation_txn.coin_outputs[1].condition.unlockhash)
        == "0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"
    )
    assert str(creation_txn.coin_outputs[1].value) == "1000840.999999501"

    # get a coin output that has already been spent
    co, creation_txn, spend_txn = c.coin_output_get("21609e91bc8dbe76a6dea0812b038bdb186ea55c60751aacb049fc91a01d7524")
    assert spend_txn is not None
    assert co is not None
    assert creation_txn is not None
    assert co.id == "21609e91bc8dbe76a6dea0812b038bdb186ea55c60751aacb049fc91a01d7524"
    assert str(co.value) == "1000842.999999501"
    assert (
        str(co.condition.unlockhash) == "0107e83d2bd8a7aad7ab0af0c0a0f1f116fb42335f64eeeb5ed1b76bd63e62ce59a3872a7279ab"
    )
    assert str(creation_txn.id) == "e6aba8ef554873e5a2bb8eea69821ebe50b821123756e5b125aaed7e3b16550b"
    assert len(creation_txn.coin_inputs) == 14
    assert [str(ci.parentid) for ci in creation_txn.coin_inputs[:3]] == [
        "4be59838a2baaf69afbc558e961aae584f69b74ab72321799f380d02d5adea01",
        "6eb896edab9539b41077a7fb540a4987d5e8b434ec77e150c1e571d2883652f2",
        "0ffc3aceee0f3f695d1173056998e49e964c72c6b9d9ce08258f51cce6d9cd18",
    ]
    assert [str(ci.parentid) for ci in creation_txn.coin_inputs[-2:]] == [
        "5ff190d50ea0d63ecfdd1500aa146344864c82512e1492947405552e1689d31a",
        "63891de50dcb285689e1cd02618917ab9df4c6001f14e63532a5a75716ec0b6c",
    ]
    assert len(creation_txn.coin_outputs) == 1
    assert creation_txn.coin_outputs[0] == co
    assert str(spend_txn.id) == "564a6d97b2d2f635ef26af90ab73268bbe7433c05d9f63a2f0b86615aabd4dc1"
    assert len(spend_txn.coin_inputs) == 1
    assert spend_txn.coin_inputs[0].parentid == co.id
