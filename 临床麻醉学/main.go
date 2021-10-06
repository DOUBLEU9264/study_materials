package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

var alphabet = "ABCDEFGHIJK"

func main() {
	fmt.Println("开始...")

	fileName := "A选择.txt"
	destFileName := "目标文件.txt"

	// 创建目标文件
	os.Remove(destFileName)
	destFile, err := os.Create(destFileName)
	if err != nil {
		log.Fatalf("创建文件%s失败：%v", destFileName, err)
	}

	// 读取文件返回字符串切片
	linesPtr, err := readFile(fileName)
	if err != nil {
		log.Fatalf("打开文件%s失败：%v", fileName, err)
	}

	lines := *linesPtr

	// 获取第一行的答案
	ans := strings.Split(lines[0], "\t")
	// 获取题目正文
	lines = lines[1:]

	// 判断题目和答案数是否相等
	if len(lines) != len(ans) {
		log.Fatal("题目和答案数不相等")
	}

	// 处理题目
	err = procLine(destFile, &lines, &ans)
	if err != nil {
		log.Fatalf("写入题目时出现错误：%v", err)
	}

	fmt.Println("结束")
}

// 读取文件按行返回字符串切片和错误
func readFile(fileName string) (*[]string, error) {
	b, err := os.ReadFile(fileName)
	if err != nil {
		return nil, err
	}

	arr := strings.Split(string(b), "\r\n")
	return &arr, nil
}

// 处理每一行
func procLine(destFile *os.File, lines, ans *[]string) error {
	for i, line := range *lines {
		lineCells := strings.Split(line, "\t")

		title := lineCells[0]
		options := lineCells[1:]

		ansIndex := strings.Index(alphabet, (*ans)[i])
		if ansIndex == -1 {
			log.Fatalf("未定位到该选项：第%d个，%s", i, (*ans)[i])
		}

		if len(options) < ansIndex {
			return fmt.Errorf("该行题目%s未达到最低答案个数：%d", line, ansIndex)
		}

		fmt.Fprintf(destFile, "%d\t%s{{c1::}}\t%s\t%d\n", i+1, title, strings.Join(options, "||"), ansIndex)
	}

	return nil
}
