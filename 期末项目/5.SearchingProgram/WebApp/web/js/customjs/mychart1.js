var colors = ['#5793f3', '#d14a61', '#675bba'];

var x_alias = ['1w', '2w', '3w', '4w', '5w', '6w', '7w', '8w', '9w', '10w',
                '11w', '12w', '13w', '14w', '15w', '16w', '17w', '18w', '19w', '20w',
                '21w', '22w', '23w', '24w', '25w', '26w', '27w', '28w', '29w', '30w',
                '31w', '32w', '33w', '34w', '35w', '36w', '37w', '38w', '39w', '40w',
                '41w', '42w', '43w', '44w', '45w', '46w', '47w', '48w', '49w', '50w',
                '51w', '52w', '53w', '54w', '55w', '56w', '57w', '58w', '59w', '60w',
                '61w', '62w', '63w', '64w', '65w', '66w', '67w', '68w', '69w', '70w'
    ]

var option_axes = {
    title: {
        text: '轮对数据检测'
    },
    color: colors,

    tooltip: {
        trigger: 'none',
        axisPointer: {
            type: 'cross'
        }
    },
    legend: {
        data: ['50%', '60%', '70%', '80%']
    },
    grid: {
        top: 70,
        bottom: 50
    },
    xAxis: [
        {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            axisLine: {
                onZero: false,
                lineStyle: {
                    color: colors[1]
                }
            },
            axisPointer: {
                label: {
                    formatter: function (params) {
                        return '检测值  ' + params.value
                            + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                    }
                }
            },
            data: x_alias
        },
        {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            axisLine: {
                onZero: false,
                lineStyle: {
                    color: colors[0]
                }
            },
            axisPointer: {
                label: {
                    formatter: function (params) {
                        return '检测值  ' + params.value
                            + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                    }
                }
            },
            data: x_alias
        },
        {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            axisLine: {
                onZero: false,
                lineStyle: {
                    color: colors[0]
                }
            },
            axisPointer: {
                label: {
                    formatter: function (params) {
                        return '检测值  ' + params.value
                            + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                    }
                }
            },
            data: x_alias
        },
        {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            axisLine: {
                onZero: false,
                lineStyle: {
                    color: colors[0]
                }
            },
            axisPointer: {
                label: {
                    formatter: function (params) {
                        return '检测值  ' + params.value
                            + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                    }
                }
            },
            data: x_alias
        },
        {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            axisLine: {
                onZero: false,
                lineStyle: {
                    color: colors[0]
                }
            },
            axisPointer: {
                label: {
                    formatter: function (params) {
                        return '检测值  ' + params.value
                            + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                    }
                }
            },
            data: x_alias
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    series: [
        {
            name: '50%',
            type: 'line',
            xAxisIndex: 1,
            smooth: true,
            data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
        },
        {
            name: '60%',
            type: 'line',
            smooth: true,
            data: [3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7]
        },
        {
            name: '70%',
            type: 'line',
            smooth: true,
            data: [3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7]
        },
        {
            name: '80%',
            type: 'line',
            smooth: true,
            data: [3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7]
        },
        {
            name: '90%',
            type: 'line',
            smooth: true,
            data: [3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7]
        }
    ]
};


// 基于准备好的dom，初始化echarts实例
var myChart_axes = echarts.init(document.getElementById('main-line'));

// 使用刚指定的配置项和数据显示图表。
myChart_axes.setOption(option);
