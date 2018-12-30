'use strict'
//chart page 3 charts settings

var colors = ['#5793f3', '#d14a61', '#675bba', '#005ab5', '#006000'];

var x_alias = ['1w', '2w', '3w', '4w', '5w', '6w', '7w', '8w', '9w', '10w',
                '11w', '12w', '13w', '14w', '15w', '16w', '17w', '18w', '19w', '20w',
                '21w', '22w', '23w', '24w', '25w', '26w', '27w', '28w', '29w', '30w',
                '31w', '32w', '33w', '34w', '35w', '36w', '37w', '38w', '39w', '40w'
    ]

var option_axes = {
    title: {
        text: '32标准轮对数据分析'
    },
    color: colors,

    tooltip: {
        trigger: 'none',
        axisPointer: {
            type: 'cross'
        }
    },
    legend: {
        data: ['50%', '60%', '70%', '80%', '90%']
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
                    color: colors[0]
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
                    color: colors[1]
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
                    color: colors[2]
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
                    color: colors[3]
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
                    color: colors[4]
                }
            },
            data: x_alias
        }
    ],
    yAxis: [
        {
            type: 'value',
            scale: true,
            label: '检测值'
        }
    ],
    series: [
        {
            name: '50%',
            type: 'line',
            xAxisIndex: 0,
            smooth: true,
            data: [31.05,30.96,30.73,30.52,30.37,30.25,30.1,29.97,29.65,29.73,29.52,29.46,29.38,29.41,29.33,29.13,29.24,29.38,29.43,29.45,29.43,29.46,29.36,29.28,29.34,29.41,29.21,29.14,29.08,29.2,29.29,29.22,29.35,29.33,29.24,29.26,29.31,29.27,29.21,29.32]
        },
        {
            name: '60%',
            type: 'line',
            // xAxisIndex: 1,
            smooth: true,
            data: [31.12,31.03,30.83,30.6,30.44,30.32,30.18,30.05,29.7,29.81,29.63,29.54,29.48,29.53,29.42,29.27,29.347,29.46,29.51,29.53,29.48,29.53,29.42,29.38,29.44,29.49,29.29,29.22,29.16,29.24,29.38,29.28,29.41,29.43,29.32,29.33,29.37,29.34,29.28,29.37]
        },
        {
            name: '70%',
            type: 'line',
            // xAxisIndex: 3,
            smooth: true,
            data: [31.23,31.16,31.01,30.73,30.58,30.51,30.34,30.19,29.84,29.98,29.87,29.74,29.71,29.79,29.62,29.51,29.55,29.67,29.65,29.69,29.61,29.71,29.58,29.57,29.61,29.67,29.44,29.45,29.34,29.44,29.51,29.45,29.58,29.62,29.51,29.49,29.51,29.51,29.43,29.51]
        },
        {
            name: '80%',
            type: 'line',
            // xAxisIndex: 4,
            smooth: true,
            data: [31.43,31.31,31.17,30.89,30.72,30.7,30.58,30.44,30.02,30.25,30.31,30,29.95,30.12,29.9,29.71,29.79,29.9,29.81,29.88,29.78,29.88,29.73,29.76,29.86,29.86,29.66,29.67,29.56,29.62,29.71,29.72,29.8,29.89,29.73,29.72,29.74,29.74,29.63,29.72]
        },
        {
            name: '90%',
            type: 'line',
            // xAxisIndex: ,
            smooth: true,
            data: [31.64,31.54,31.39,31.14,30.94,30.95,30.99,30.71,30.38,30.69,30.74,30.41,30.37,30.66,30.24,30.07,30.11,30.21,30.05,30.31,30.05,30.18,30.04,30.04,30.16,30.14,30.03,30.06,29.94,29.9,29.95,29.99,29.97,30.1,29.95,29.98,30.02,29.99,29.95,30.14]
        }
    ]
};

var option_30 = {
    title: {
        text: '30标准轮对数据分析'
    },
    color: colors,

    tooltip: {
        trigger: 'none',
        axisPointer: {
            type: 'cross'
        }
    },
    legend: {
        data: ['50%', '60%', '70%', '80%', '90%']
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
                    color: colors[0]
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
                    color: colors[1]
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
                    color: colors[2]
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
                    color: colors[3]
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
                    color: colors[4]
                }
            },
            data: x_alias
        }
    ],
    yAxis: [
        {
            type: 'value',
            scale: true,
            label: '检测值'
        }
    ],
    series: [
        {
            name: '50%',
            type: 'line',
            xAxisIndex: 0,
            smooth: true,
            data: [29.94,29.84,29.9,29.95,29.91,30,29.97,30.01,29.91,29.96,29.9,30.16,30.08,30.17,30.19,30.26,30.21,30.19,30.27,30.44,30.47,30.42,30.34,30.53,30.42,30.4,30.12,30.35,30.2,30.05,30.02,30.04,30.08,30.04,30,30.13,30.08,30.18,30.11,30.35,30.34
]
        },
        {
            name: '60%',
            type: 'line',
            // xAxisIndex: 1,
            smooth: true,
            data: [
                29.97,29.89,29.97,29.99,29.94,30.04,30.02,30.05,29.99,30.04,30,30.24,30.16,30.26,30.25,30.33,30.29,30.29,30.36,30.52,30.55,30.56,30.52,30.66,30.55,30.63,30.3,30.64,30.35,30.21,30.07,30.09,30.11,30.07,30.04,30.15,30.12,30.22,30.14,30.39
            ]
        },
        {
            name: '70%',
            type: 'line',
            // xAxisIndex: 3,
            smooth: true,
            data: [
                30.04,29.98,30.08,30.07,30.02,30.15,30.11,30.15,30.12,30.18,30.12,30.38,30.31,30.45,30.36,30.49,30.45,30.45,30.58,30.66,30.68,30.81,30.76,30.91,30.82,30.89,30.66,31.03,30.54,30.84,30.33,30.22,30.23,30.15,30.12,30.25,30.29,30.38,30.2,30.65
            ]
        },
        {
            name: '80%',
            type: 'line',
            // xAxisIndex: 4,
            smooth: true,
            data: [
                30.13,30.08,30.18,30.16,30.1,30.28,30.2,30.26,30.25,30.36,30.24,30.52,30.48,30.62,30.52,30.69,30.62,30.64,30.83,30.87,30.9,31.12,31.02,31.19,31.04,31.23,30.99,31.29,31.11,31.36,31.11,30.47,31.35,30.34,30.22,30.41,30.7,31.82,30.27,31.89
            ]
        },
        {
            name: '90%',
            type: 'line',
            // xAxisIndex: ,
            smooth: true,
            data: [
                30.27,30.22,30.33,30.29,30.21,30.5,30.34,30.39,30.38,30.61,30.37,30.76,30.67,30.92,30.71,30.92,30.83,30.88,31.07,31.08,31.17,31.37,31.36,31.48,31.34,31.71,31.51,31.65,31.48,31.84,31.65,31,31.97,32,30.38,31.93,32.09,32.05,30.32,32.16,32.23
            ]
        }
    ]
};


// 基于准备好的dom，初始化echarts实例
var myChart_axes = echarts.init(document.getElementById('main-32'));

// 使用刚指定的配置项和数据显示图表。
myChart_axes.setOption(option_axes);
