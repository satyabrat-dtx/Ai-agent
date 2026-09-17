# DB2ADMIN.COSTSIMROUTESTEP

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 79
- **Primary key**: `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE`, `TABLEINDEX`, `SUBUNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196276

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SIMULATIONCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SIMULATIONCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 4 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 5 | `PLANTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 6 | `SUBUNIQUEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `COSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 9 | `ROUTEINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 10 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 11 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 12 | `OPERATIONCODE` | CHAR(8) | NOT NULL |  |  |  |
| 13 | `WORKCENTERANDOPERATTRIBUTESCOD` | CHAR(20) |  |  |  |  |
| 14 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 15 | `EFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 16 | `EFFICIENCYAPPLY` | CHAR(1) |  |  |  |  |
| 17 | `STDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `STDUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `REPETITIONNUMBER` | DECIMAL(15,5) |  |  |  |  |
| 20 | `INITQTYPRIMEUOM` | DECIMAL(20,10) |  |  |  |  |
| 21 | `FINALQTYPRIMEUOM` | DECIMAL(20,10) |  |  |  |  |
| 22 | `INITQTYSECONDUOM` | DECIMAL(20,10) |  |  |  |  |
| 23 | `FINALQTYSECONDUOM` | DECIMAL(20,10) |  |  |  |  |
| 24 | `WASTEQTYINPRIMARYUOM` | DECIMAL(20,10) |  |  |  |  |
| 25 | `WASTEQTYINSECONDARYUOM` | DECIMAL(20,10) |  |  |  |  |
| 26 | `TOTALTIME` | DECIMAL(20,10) |  |  |  |  |
| 27 | `LOSSINCREASETYPE1CODE` | CHAR(3) |  |  |  |  |
| 28 | `LOSSINCREASE1` | DECIMAL(15,5) |  |  |  |  |
| 29 | `LOSSINCREASEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 30 | `LOSSINCREASETYPE2CODE` | CHAR(3) |  |  |  |  |
| 31 | `LOSSINCREASE2` | DECIMAL(15,5) |  |  |  |  |
| 32 | `LOSSINCREASEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 33 | `LOSSINCREASETYPE3CODE` | CHAR(3) |  |  |  |  |
| 34 | `LOSSINCREASE3` | DECIMAL(15,5) |  |  |  |  |
| 35 | `LOSSINCREASEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 36 | `LOSSINCREASETYPE4CODE` | CHAR(3) |  |  |  |  |
| 37 | `LOSSINCREASE4` | DECIMAL(15,5) |  |  |  |  |
| 38 | `LOSSINCREASEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 39 | `LOSSINCREASETYPE5CODE` | CHAR(3) |  |  |  |  |
| 40 | `LOSSINCREASE5` | DECIMAL(15,5) |  |  |  |  |
| 41 | `LOSSINCREASEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 42 | `LOSSINCREASETYPE6CODE` | CHAR(3) |  |  |  |  |
| 43 | `LOSSINCREASE6` | DECIMAL(15,5) |  |  |  |  |
| 44 | `LOSSINCREASEREFUOM6CODE` | CHAR(3) |  |  |  |  |
| 45 | `LOSSINCREASETYPE7CODE` | CHAR(3) |  |  |  |  |
| 46 | `LOSSINCREASE7` | DECIMAL(15,5) |  |  |  |  |
| 47 | `LOSSINCREASEREFUOM7CODE` | CHAR(3) |  |  |  |  |
| 48 | `LOSSINCREASETYPE8CODE` | CHAR(3) |  |  |  |  |
| 49 | `LOSSINCREASE8` | DECIMAL(15,5) |  |  |  |  |
| 50 | `LOSSINCREASEREFUOM8CODE` | CHAR(3) |  |  |  |  |
| 51 | `TIMETYPE1CODE` | CHAR(3) |  |  |  |  |
| 52 | `TIME1` | DECIMAL(10,5) |  |  |  |  |
| 53 | `TIMEUNIT1` | CHAR(2) |  |  |  |  |
| 54 | `TIMEREFQTY1` | DECIMAL(15,5) |  |  |  |  |
| 55 | `TIMEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 56 | `TIMETYPE2CODE` | CHAR(3) |  |  |  |  |
| 57 | `TIME2` | DECIMAL(10,5) |  |  |  |  |
| 58 | `TIMEUNIT2` | CHAR(2) |  |  |  |  |
| 59 | `TIMEREFQTY2` | DECIMAL(15,5) |  |  |  |  |
| 60 | `TIMEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 61 | `TIMETYPE3CODE` | CHAR(3) |  |  |  |  |
| 62 | `TIME3` | DECIMAL(10,5) |  |  |  |  |
| 63 | `TIMEUNIT3` | CHAR(2) |  |  |  |  |
| 64 | `TIMEREFQTY3` | DECIMAL(15,5) |  |  |  |  |
| 65 | `TIMEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 66 | `TIMETYPE4CODE` | CHAR(3) |  |  |  |  |
| 67 | `TIME4` | DECIMAL(10,5) |  |  |  |  |
| 68 | `TIMEUNIT4` | CHAR(2) |  |  |  |  |
| 69 | `TIMEREFQTY4` | DECIMAL(15,5) |  |  |  |  |
| 70 | `TIMEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 71 | `TIMETYPE5CODE` | CHAR(3) |  |  |  |  |
| 72 | `TIME5` | DECIMAL(10,5) |  |  |  |  |
| 73 | `TIMEUNIT5` | CHAR(2) |  |  |  |  |
| 74 | `TIMEREFQTY5` | DECIMAL(15,5) |  |  |  |  |
| 75 | `TIMEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 76 | `CALCULATEDTIME2` | DECIMAL(10,5) |  |  |  |  |
| 77 | `CALCULATEDTIME3` | DECIMAL(10,5) |  |  |  |  |
| 78 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COSTSIMULATION_SIMULATION` | `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE` | [`COSTSIMULATION`](../COSTING/COSTSIMULATION.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `COSTSIMROUTESTEP.COMPANYCODE = COSTSIMULATION.COMPANYCODE AND COSTSIMROUTESTEP.SIMULATIONCOUNTERCODE = COSTSIMULATION.COUNTERCODE AND COSTSIMROUTESTEP.SIMULATIONCODE = COSTSIMULATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTSIMROUTESTEPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SIMULATIONCOUNTERCODE,
       t.SIMULATIONCODE,
       t.TABLEINDEX,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.SUBUNIQUEID,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.ROUTEINDEX,
       t.STEPNUMBER,
       t.WORKCENTERCODE
FROM   DB2ADMIN.COSTSIMROUTESTEP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
