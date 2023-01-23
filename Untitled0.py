{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP9AZToZfYLI1YhKtQrqxAf"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LAxNQhUM-r-Z",
        "outputId": "9869fcb8-4d94-4f86-93bc-ba1d9d1b6acf"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n"
          ]
        }
      ],
      "source": [
        "\n",
        "\"\"\"\n",
        "모달리스 창\n",
        "\n",
        "(개별) 현재값\n",
        "관심종목 현재값\n",
        "  순서 조정\n",
        "실시간 그래프\n",
        "  전고점 전저점\n",
        "  확대 축소\n",
        "\n",
        "\"\"\"\n",
        "\n",
        "class nowValue:\n",
        "  def __init__(self):\n",
        "    self.value = 0\n",
        "\n",
        "  def update(self, recentValue):\n",
        "    self.value = recentValue\n",
        "    return self.value\n"
      ]
    }
  ]
}