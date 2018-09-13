# animalAI
講義などで興味を持ったCNNについて独習

内容については、まとまった時間ができ次第書きます。

[Udemy](https://www.udemy.com/tensorflow-advanced/)を参考にしながら進めています。

GPUください。

# Usage
自分はAnacondaで仮想環境を作って動かしました。

`tensorflow`や`pillow`、`keras`や`flask`を順次`pip install `してください。

`python -m flask run`と実行すると、サーバーが起動し、http://127.0.0.1:5000 にアクセスすると動作します。



# Progress
## 2018-09-12 まで
- クローリングから、前処理を済ませた。
  - [前処理メモ](https://github.com/hysy/animalAI/blob/master/_etc/%E5%89%8D%E5%87%A6%E7%90%86%E3%83%A1%E3%83%A2.txt)
  - [boar](https://github.com/hysy/animalAI/tree/master/boar)
  - [monkey](https://github.com/hysy/animalAI/tree/master/monkey)
  - [crow](https://github.com/hysy/animalAI/tree/master/crow)

- CNNのCPU実行まで実装した。
  - [AnimalAI/CNNLossAcc](https://github.com/hysy/animalAI/tree/master/CNNLossAcc) を参照。

## 2018-09-13
- 画像の回転・反転により、学習データを増やし、学習中
