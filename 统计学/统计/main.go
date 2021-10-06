package main

import (
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

type typeIndex struct {
	index    int
	quesType int // 0选择题 1判断题 2简答 3分析
}

func main() {
	lines, err := readlines("练习册.txt")
	if err != nil {
		log.Println(err)
		return
	}

	indexList := getIndex(lines)

	选择题 := ""
	判断题 := ""
	简答 := ""
	分析 := ""

	for i := len(indexList) - 1; i >= 0; i-- {
		ti := indexList[i]
		switch ti.quesType {
		case 0:
			选择题 = strings.Join(lines[ti.index:], "\n") + "\n\n" + 选择题
		case 1:
			判断题 = strings.Join(lines[ti.index:], "\n") + "\n\n" + 判断题
		case 2:
			简答 = strings.Join(lines[ti.index:], "\n") + "\n\n" + 简答
		case 3:
			分析 = strings.Join(lines[ti.index:], "\n") + "\n\n" + 分析
		}
		lines = lines[:ti.index]
	}

	f, _ := os.Create("new.txt")
	defer f.Close()
	fmt.Fprintln(f, 选择题, "\n")
	fmt.Fprintln(f, 判断题, "\n")
	fmt.Fprintln(f, 简答, "\n")
	fmt.Fprintln(f, 分析, "\n")
}

func readlines(path string) ([]string, error) {
	fmt.Println("读取文件")
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	b, err := io.ReadAll(f)
	if err != nil {
		return nil, err
	}

	s := string(b)
	return strings.Split(s, "\r\n"), nil
}

func getIndex(lines []string) []typeIndex {
	fmt.Println("解析题目类型索引")
	var indexList []typeIndex

	for i, l := range lines {
		if strings.TrimSpace(l) == "" {
			continue
		}

		if !strings.ContainsRune("一二三四五", []rune(l)[0]) {
			continue
		}

		var ti typeIndex

		switch {
		case strings.Contains(l, "选择"):
			ti.quesType = 0

		case strings.Contains(l, "判断"):
			ti.quesType = 1

		case strings.Contains(l, "简答"):
			ti.quesType = 2

		case strings.Contains(l, "分析"):
			ti.quesType = 3

		default:
			fmt.Println(l)
			continue
		}

		ti.index = i
		indexList = append(indexList, ti)
	}

	return indexList
}
