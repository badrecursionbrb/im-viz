<template>
    <svg ref="dfgsvgref"></svg>
</template>

<script>
// As a basis of the following graph the examples on https://marvl.infotech.monash.edu/webcola/index.html served 


import * as d3 from "../WebCola/extern/d3v4";
import "../WebCola/cola.min.js";
import "../WebCola/style.css";
import Store from "../store";
import * as colax from "webcola"


export default {
    name: "PackDFGComp",
    props: ['triggerChange'],
    watch: {
        triggerChange: function (dfgData) {
            console.log("rendering dfg data from child " + (new Date).toLocaleTimeString());
            this.update(dfgData);
        }
    },
    data() {
        return {
            //dfgData: Store.state.miserablesJson,
            linkDistance: 100,
            iterationsUnc: 10,
            iterationsConstr: 10,
            iterationsAllConstr: 10,
            nodeSize: 12
        }
    },
    created() {
        //this.zoom= d3.zoom().on('zoom', this.zoomed);
        // this.zoom = d3.zoom()
        //     .scaleExtent([1/4, 4])
        //     .on('zoom', this.zoomed)
    },
    mounted() {
        console.log("mounting dfg ...");
        // initializing with test data
        //this.update(this.dfgData);
    },
    methods: {
        renderChart(graph) {
            // This is the main method for rendering the DFG chart, it is an adaptation of one 
            // of the examples of the WebCola package
            var jaccardLinkLengths = 80;

            console.log("renderChart start ... " + (new Date).toLocaleTimeString())

            let nodeSize = this.nodeSize;

            let margin = { top: 60, bottom: 60, left: 60, right: 60 }
            var width = this.$refs.dfgsvgref.clientWidth - margin.left - margin.right,
                height = this.$refs.dfgsvgref.clientHeight - margin.top - margin.bottom;

            var color = d3.scaleOrdinal(d3.schemeCategory20);

            var d3x = d3
            var cola = colax.d3adaptor(d3x)
                //.linkDistance(80)
                .avoidOverlaps(true)
                .handleDisconnected(true)
                .size([width, height]);

            var svg = d3x.select("#dfgGraph")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
            // .call(d3.zoom().on("zoom", function () {
            //         d3.attr("transform", d3.event.transform)
            // }));
            var g = svg.append("g");

            this.zoom = d3.zoom()
                .extent([[0, 0], [width, height]])
                .scaleExtent([0.1, 8])
                .on("zoom", this.zoomed);

            svg.call(this.zoom);
            //svg.call(this.zoom)

            // var dfgGraphic = svg.append('g')
            //                 .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')
            //                 .attr('width', width)
            //                 .attr('height', height);

            console.log(graph)
            console.log(graph.nodes)
            console.log(graph.links)

            cola
                //.convergenceThreshold(0.1)
                .nodes(graph.nodes)
                .links(graph.links)
                .jaccardLinkLengths(jaccardLinkLengths)
                //.start(this.iterationsUnc, this.iterationsConstr, this.iterationsAllConstr);
                .start(10, 10, 10);

            g.append("defs").append("marker")
                //.append("line")
                .attr("id", "dir-arrow")
                //.style("stroke-width", function (d) { return Math.sqrt(d.value); });
                //.append('svg:defs').append('svg:marker')
                //.attr('class', "end-marker")
                .attr("viewBox", "0 -8 16 16")
                .attr("refX", 20)
                .attr("refY", 0)
                .attr('markerWidth', 24)
                .attr('markerHeight', 28)
                .attr('orient', 'auto')
                // .append('svg:path')
                .attr('opacity', "80%")
                .attr('fill', 'grey')
                .append("path")
                .attr('d', 'M0,-5L10,0L0,5')
                .attr('stroke-width', '10px')
                .attr('fill', 'grey');

            var linkSelection = g.selectAll("line")
                .data(graph.links)
            var link = linkSelection
                .enter().append("line")
                .attr("stroke", "grey")
                .attr("marker-end", "url(#dir-arrow)");

            var linkLabelSelection = g.selectAll(".edgelabel")
                .data(graph.links);
            var linkLabel = linkLabelSelection.enter()
                .append('text')
                .attr("class", "linkLabel")
                .attr("font-size", "14px")
                .text(function (d) { return d.count; });

            var nodeSelection = g.selectAll(".node")
                .data(graph.nodes)
            var node = nodeSelection
                .enter().append("circle")
                .attr("class", "node")
                .attr("r", nodeSize)
                .style("fill", function (d) { return color(d.group); })
                .call(cola.drag);

            var labelSelection = g.selectAll(".label")
                .data(graph.nodes)
            var label = labelSelection
                .enter().append("text")
                .attr("class", "label")
                .attr("font-size", "16px")
                .text(function (d) { return d.value; });

            node.append("title")
                .text(function (d) { return d.id; });

            cola.on("tick", function () {
                link.attr("x1", function (d) { return d.source.x; })
                    .attr("y1", function (d) { return d.source.y; })
                    .attr("x2", function (d) { return d.target.x; })
                    .attr("y2", function (d) { return d.target.y; });
                linkLabel.attr("x", function (d) {
                    var xdiff = d.source.x - d.target.x;
                    if (xdiff < 0) {
                        // target is larger
                        return d.source.x + 0.6 * -1 * xdiff;
                    }
                    else {
                        // source is larger
                        return d.target.x + 0.4 * xdiff;
                    }
                })
                    .attr("y", function (d) {
                        var ydiff = d.source.y - d.target.y;
                        if (ydiff < 0) {
                            // target is larger
                            return d.source.y + 0.6 * -1 * ydiff;
                        }
                        else {
                            // source is larger
                            return d.target.y + 0.4 * ydiff;
                        }
                    });

                node.attr("cx", function (d) { return d.x; })
                    .attr("cy", function (d) { return d.y; });


                label.attr("x", function (d) { return d.x - 0.5 * nodeSize; })
                    .attr("y", function (d) { return d.y + 0.5 * nodeSize });
            });

            // if needed put transition below this line 

            // removing the elements not present anymore in updated graph
            nodeSelection.exit().remove();
            linkSelection.exit().remove();
            labelSelection.exit().remove();
            linkLabelSelection.exit().remove();
        },
        update(newData) {
            // This method updates the DFG graph, triggering the renderChart method 

            //this.beforeUpdate(this.dfgData);
            d3.select("#dfgGraph").selectAll("*").remove();

            this.dfgData = newData;
            this.renderChart(newData);
            this.reset();
        },
        // performZoom(){
        //     d3.attr('transform', d3.event.transform);
        // },
        // initZoom() {
        //         d3.select('#dfgGraph').call(d3.zoom()
        //         .on('zoom', this.performZoom));
        // },
        reset() {
            // This method implements that the graph is reset to identity 

            // d3.select('#dfgGraph').select('g')
            //     .transition()
            //     .duration(750)
            //      .call(this.zoom)
            d3.select('#dfgGraph').select('g').call(this.zoom.transform, d3.zoomIdentity);
            // var bboxOfGroup = d3.select('#dfgGraph').select('g').node().getBBox();
            // var halfXGroup = bboxOfGroup.width / 2;
            // var halfYGroup = bboxOfGroup.height / 2;
            // var divHeight = this.$refs.dfgsvgref.parentNode.clientHeight;
            // var divWidth = this.$refs.dfgsvgref.parentNode.clientWidth;
            // var bbox = this.$refs.dfgsvgref.getBBox();
            // var middleX = bbox.x + (bbox.width / 2);
            // var middleY = bbox.y + (bbox.height / 2);
            // var transX = divWidth/4 - halfXGroup;
            // var transY = divHeight/4 - halfYGroup;
            //d3.select('#dfgGraph').select('g').attr('transform',  `translate(${transX}, ${transY})`);
            d3.select('#dfgGraph').select('g').attr('transform', `translate(50, 50)`)


        },
        zoomed() {
            // This method implements zooming behaviour 

            console.log("trying zooming");
            d3.select('#dfgGraph').select('g').attr("transform", d3.event.transform);
            //d3.select('#dfgGraph').select('g').attr("transform", e.transform);
            // d3.select('#dfgGraph').select('g').attr("transform", 'translate(' + d3.event.translate + ')'
            // +   'scale(' + d3.event.scale     + ')');
        },
        // initZoom() {
        //         d3.select('#dfgGraph').select('g')
        //             .call(this.zoom);
        //     },
        // beforeUpdate(data) {
        //     console.log("running beforeUpdate");
        //     var svg = d3.select("svg");
        //     var nodes = svg.selectAll(".node").data(data).exit().remove();
        //     var lines = svg.selectAll(".line").data(data).exit().remove();
        // }
    }
};
</script>

<style>
#dfgsvg {
    display: flex;
    flex-grow: 1;
}

.node {
    stroke: #fff;
    stroke-width: 1.5px;
}

.link {
    stroke: #999;
    stroke-opacity: .8;
}</style>