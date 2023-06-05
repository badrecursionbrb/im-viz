<template>
  <v-table id="table_dfg" density="compact">
    <thead>
      <tr>
        <th class="text-left">
          Trace
        </th>
        <th class="text-left">
          Count
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in tableDataChild" :key="item.trace">
        <td class="text-left tableText">{{ item.trace }}</td>
        <td class="text-left tableText">{{ item.count }}</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script>

export default {
  name: "TableComp",
  props: ['triggerChange', 'tableDataChild'],

  watch: {
    triggerChange: function (tableData) {
      console.log("rendering table data from child " + (new Date).toLocaleTimeString());
      console.log("tableData: " + tableData);
      this.update(tableData);
    }
  },
  mounted() {
    console.log("table mounted");
  },
  data() {
    return {
      tableData: null,
    }
  },
  methods: {
    update(tableData) {
      // This method updates the table  

      console.log("table Data from tableComp: " + tableData);
      this.tableData = tableData;
      // for (let i = 0; i < tableData.length; i++) {
      //   console.log(this.tableData[i]);
      // }
    }
  }
}
</script>
<style>
#table_dfg{
  font-weight: 600 !important;
}
.v-tabs.v-tabs--horizontal {
  background: black !important;
}

</style>

