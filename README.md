# animalAI
講義などで興味を持ったCNNについて独習しました。

<br />

## Abstract
画像をKerasのCNNで学習した分類機で分類します。

学習モデルは、[Keras](https://keras.io/getting-started/sequential-model-guide/) の [Example](https://github.com/keras-team/keras/tree/master/examples) の一番シンプルなCNN [cifar10_cnn.py](https://github.com/keras-team/keras/blob/master/examples/cifar10_cnn.py) を使用しました


学習データは、flickrからクローリングしたイノシシ（boar）、猿（monkey）、カラス（crow）のみです。

関係ない画像をアップロードすると一番近い動物が出力されます。

<br />

## Accuracy Improvement
今回は精度向上も実装しました。（向上できなかった）

パラメータの調整などは行わず、画像データを増やしてみました。

画像データの一部を回転、反転させることで1枚が16枚分になっています。

![image](https://github.com/hysy/animalAI/blob/master/_etc/%E5%8F%8D%E8%BB%A2.PNG)

<br />

## Classifier Type
分類器は大きく分けて、通常版と増幅版（↑参照）の2種類を作成しました。

また、↑のそれぞれの分類器に対して、[epoch数](http://st-hakky.hatenablog.com/entry/2017/01/17/165137) (=1つの訓練データを何回繰り返して学習させるか)を `1, 20, 50, 100` と変化させ、8種類の分類器を作成しました。

分類機は1つ300MBぐらいになったので、精度の良かった4つの分類器（epoch = `50, 100`）のみ残っています。

<br />

参考: [Udemy](https://www.udemy.com/tensorflow-advanced/)

# Environment

| Equipment | Name |
|:-:|:-:|
| OS | Windows 7 Professional (64bit) |
| Processor | Intel Xeon CPU E3-1225 3.30GHz |
| RAM | 16GB | 


# Usage
自分はAnacondaで仮想環境を作って動かしました。

- 環境設定
  - `tensorflow`や`pillow`、`keras`や`flask`、`numpy`、`sklearn`を順次`pip install `します。
  - その後、`set FLASK_APP=predict.py`(Windows版)などで、`FLASK_APP`に`predict.py` へのpathを通します。
  - `python -m flask run`と実行すると、サーバーが起動し、http://127.0.0.1:5000 にアクセスすると動作します。

- 実行
  - http://127.0.0.1:5000 にアクセスすると、以下のような画面が表示されます。
    ![image](https://github.com/hysy/animalAI/blob/master/_etc/%E5%AE%9F%E8%A1%8C%E7%94%BB%E9%9D%A21.PNG)
  - 画像ファイル（png, jpg, gif）を選択し、Uploadボタンを押します。
  - サーバー側で分類後、結果が出力されます。
  
    ![image](https://github.com/hysy/animalAI/blob/master/_etc/%E5%AE%9F%E8%A1%8C%E7%94%BB%E9%9D%A22-boar.PNG)
  - Uploadした画像は`./uploads`に保存されます。
  - `predictfile.py`の38行目の分類器の指定部分を変更すると、違う分類器で実行できます。
    - 通常版: `CNNLossAcc/animal_cnn[epoch数].h5`
    - 増量版: `CNNLossAcc_aug/animal_cnn_aug[epoch数].h5`
      - 増量版の学習データは、画像データの一部を回転、反転させることで1枚が16枚分になっています。
      - ちなみに、増量版のほうが精度が悪かったです。
    
# Progress
## 2018-09-12 まで
- クローリングから、前処理を済ませた。
  - [前処理メモ](https://github.com/hysy/animalAI/blob/master/_etc/%E5%89%8D%E5%87%A6%E7%90%86%E3%83%A1%E3%83%A2.txt)
  - [boar](https://github.com/hysy/animalAI/tree/master/boar)
  - [monkey](https://github.com/hysy/animalAI/tree/master/monkey)
  - [crow](https://github.com/hysy/animalAI/tree/master/crow)

- 通常版CNNのCPU実行まで実装した。
  - [AnimalAI/CNNLossAcc](https://github.com/hysy/animalAI/tree/master/CNNLossAcc) を参照。

## 2018-09-13
- 画像の回転・反転により、学習データを増やし、学習
- 増幅版CNNのCPU実行まで実装・実行した。
  - [AnimalAI/CNNLossAcc_aug](https://github.com/hysy/animalAI/tree/master/CNNLossAcc_aug) を参照。
- Webアプリの形まで作成
  - Usageを参照
- とりあえず、コース分は完成。


# Result
CPU実行なので、とりあえず前日（2018-09-12）に漬けておいた（画像複製なし、epoch=100）でやってみました。

## Correct Example

何回かやってみたところ、正面や顔のみ、全身の写真は正確に識別できました。
![image](https://github.com/hysy/animalAI/blob/master/_etc/%E5%AE%9F%E8%A1%8C%E7%94%BB%E9%9D%A22-boar.PNG)

![image](https://github.com/hysy/animalAI/blob/master/_etc/%E5%AE%9F%E8%A1%8C%E7%94%BB%E9%9D%A22-monkey.PNG)

![image](https://github.com/hysy/animalAI/blob/master/_etc/%E5%AE%9F%E8%A1%8C%E7%94%BB%E9%9D%A22-crow.PNG)

## Incorrect Example

![image](https://github.com/hysy/animalAI/blob/master/_etc/%E5%AE%9F%E8%A1%8C%E7%94%BB%E9%9D%A23-boar.PNG)

![image](https://github.com/hysy/animalAI/blob/master/_etc/%E5%AE%9F%E8%A1%8C%E7%94%BB%E9%9D%A23-monkey.PNG)

![image](https://github.com/hysy/animalAI/blob/master/_etc/%E5%AE%9F%E8%A1%8C%E7%94%BB%E9%9D%A23-crow.PNG)

# Consideration
分類に失敗した画像を見ると、毛の色のグラデーションや毛並み、撮影角度による形状など、撮影環境や学習データの影響を感じる。

増量版の精度が悪かったのは、学習データが複製したものばかりに偏ってしまったから（？）

# Prospects
上の考察から、どの位置から見ても同じような面が多く、特徴的な形をした立体（リンゴ、いちご、パイナップルなどの果物（加工前））などは高精度を出せると思う。
またやります。


# おまけ
![image](https://github.com/hysy/animalAI/blob/master/_etc/%E5%AE%9F%E8%A1%8C%E7%B5%90%E6%9E%9C4-Nanachi.PNG)
