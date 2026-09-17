# DB2ADMIN.COSTROUTESTEP

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 76
- **Primary key**: `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 12823

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 3 | `PLANTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 4 | `COSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `ROUTEINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 7 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 8 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `OPERATIONCODE` | CHAR(8) | NOT NULL |  |  |  |
| 10 | `WORKCENTERANDOPERATTRIBUTESCOD` | CHAR(20) |  |  |  |  |
| 11 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 12 | `EFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 13 | `EFFICIENCYAPPLY` | CHAR(1) |  |  |  |  |
| 14 | `STDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `STDUOMCODE` | CHAR(3) |  |  |  |  |
| 16 | `REPETITIONNUMBER` | DECIMAL(15,5) |  |  |  |  |
| 17 | `INITQTYPRIMEUOM` | DECIMAL(20,10) |  |  |  |  |
| 18 | `FINALQTYPRIMEUOM` | DECIMAL(20,10) |  |  |  |  |
| 19 | `INITQTYSECONDUOM` | DECIMAL(20,10) |  |  |  |  |
| 20 | `FINALQTYSECONDUOM` | DECIMAL(20,10) |  |  |  |  |
| 21 | `WASTEQTYINPRIMARYUOM` | DECIMAL(20,10) |  |  |  |  |
| 22 | `WASTEQTYINSECONDARYUOM` | DECIMAL(20,10) |  |  |  |  |
| 23 | `TOTALTIME` | DECIMAL(20,10) |  |  |  |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 25 | `LOSSINCREASETYPE1CODE` | CHAR(3) |  |  |  |  |
| 26 | `LOSSINCREASE1` | DECIMAL(15,5) |  |  |  |  |
| 27 | `LOSSINCREASEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 28 | `LOSSINCREASETYPE2CODE` | CHAR(3) |  |  |  |  |
| 29 | `LOSSINCREASE2` | DECIMAL(15,5) |  |  |  |  |
| 30 | `LOSSINCREASEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 31 | `LOSSINCREASETYPE3CODE` | CHAR(3) |  |  |  |  |
| 32 | `LOSSINCREASE3` | DECIMAL(15,5) |  |  |  |  |
| 33 | `LOSSINCREASEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 34 | `LOSSINCREASETYPE4CODE` | CHAR(3) |  |  |  |  |
| 35 | `LOSSINCREASE4` | DECIMAL(15,5) |  |  |  |  |
| 36 | `LOSSINCREASEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 37 | `LOSSINCREASETYPE5CODE` | CHAR(3) |  |  |  |  |
| 38 | `LOSSINCREASE5` | DECIMAL(15,5) |  |  |  |  |
| 39 | `LOSSINCREASEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 40 | `LOSSINCREASETYPE6CODE` | CHAR(3) |  |  |  |  |
| 41 | `LOSSINCREASE6` | DECIMAL(15,5) |  |  |  |  |
| 42 | `LOSSINCREASEREFUOM6CODE` | CHAR(3) |  |  |  |  |
| 43 | `LOSSINCREASETYPE7CODE` | CHAR(3) |  |  |  |  |
| 44 | `LOSSINCREASE7` | DECIMAL(15,5) |  |  |  |  |
| 45 | `LOSSINCREASEREFUOM7CODE` | CHAR(3) |  |  |  |  |
| 46 | `LOSSINCREASETYPE8CODE` | CHAR(3) |  |  |  |  |
| 47 | `LOSSINCREASE8` | DECIMAL(15,5) |  |  |  |  |
| 48 | `LOSSINCREASEREFUOM8CODE` | CHAR(3) |  |  |  |  |
| 49 | `TIMETYPE1CODE` | CHAR(3) |  |  |  |  |
| 50 | `TIME1` | DECIMAL(10,5) |  |  |  |  |
| 51 | `TIMEUNIT1` | CHAR(2) |  |  |  |  |
| 52 | `TIMEREFQTY1` | DECIMAL(15,5) |  |  |  |  |
| 53 | `TIMEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 54 | `TIMETYPE2CODE` | CHAR(3) |  |  |  |  |
| 55 | `TIME2` | DECIMAL(10,5) |  |  |  |  |
| 56 | `TIMEUNIT2` | CHAR(2) |  |  |  |  |
| 57 | `TIMEREFQTY2` | DECIMAL(15,5) |  |  |  |  |
| 58 | `TIMEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 59 | `TIMETYPE3CODE` | CHAR(3) |  |  |  |  |
| 60 | `TIME3` | DECIMAL(10,5) |  |  |  |  |
| 61 | `TIMEUNIT3` | CHAR(2) |  |  |  |  |
| 62 | `TIMEREFQTY3` | DECIMAL(15,5) |  |  |  |  |
| 63 | `TIMEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 64 | `TIMETYPE4CODE` | CHAR(3) |  |  |  |  |
| 65 | `TIME4` | DECIMAL(10,5) |  |  |  |  |
| 66 | `TIMEUNIT4` | CHAR(2) |  |  |  |  |
| 67 | `TIMEREFQTY4` | DECIMAL(15,5) |  |  |  |  |
| 68 | `TIMEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 69 | `TIMETYPE5CODE` | CHAR(3) |  |  |  |  |
| 70 | `TIME5` | DECIMAL(10,5) |  |  |  |  |
| 71 | `TIMEUNIT5` | CHAR(2) |  |  |  |  |
| 72 | `TIMEREFQTY5` | DECIMAL(15,5) |  |  |  |  |
| 73 | `TIMEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 74 | `CALCULATEDTIME2` | DECIMAL(10,5) |  |  |  |  |
| 75 | `CALCULATEDTIME3` | DECIMAL(10,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTROUTESTEP01` (COMPANYCODE, PLANTCODE, COSTGROUPCODE, COSTSCOSTGROUPCODE, PRODUCTINDEX, ROUTEINDEX, STEPNUMBER)
- `COSTROUTESTEPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TABLEINDEX,
       t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.ROUTEINDEX,
       t.STEPNUMBER,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.WORKCENTERANDOPERATTRIBUTESCOD,
       t.PRODRESERVATIONLINKGROUPCODE
FROM   DB2ADMIN.COSTROUTESTEP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
