# DB2ADMIN.COSTROUTESTEPBYDATE

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 76
- **Primary key**: `COMPANYCODE`, `PRODUCTINDEX`, `PLANTCODE`, `COSTGROUPCODE`, `COSTSCOSTGROUPCODE`, `VALIDITYDATE`, `ROUTEINDEX`, `STEPNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 238283

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `COSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `VALIDITYDATE` | DATE | NOT NULL | PK | primary_key |  |
| 6 | `ROUTEINDEX` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 7 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `STEPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
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
| 24 | `LOSSINCREASETYPE1CODE` | CHAR(3) |  |  |  |  |
| 25 | `LOSSINCREASE1` | DECIMAL(15,5) |  |  |  |  |
| 26 | `LOSSINCREASEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 27 | `LOSSINCREASETYPE2CODE` | CHAR(3) |  |  |  |  |
| 28 | `LOSSINCREASE2` | DECIMAL(15,5) |  |  |  |  |
| 29 | `LOSSINCREASEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 30 | `LOSSINCREASETYPE3CODE` | CHAR(3) |  |  |  |  |
| 31 | `LOSSINCREASE3` | DECIMAL(15,5) |  |  |  |  |
| 32 | `LOSSINCREASEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 33 | `LOSSINCREASETYPE4CODE` | CHAR(3) |  |  |  |  |
| 34 | `LOSSINCREASE4` | DECIMAL(15,5) |  |  |  |  |
| 35 | `LOSSINCREASEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 36 | `LOSSINCREASETYPE5CODE` | CHAR(3) |  |  |  |  |
| 37 | `LOSSINCREASE5` | DECIMAL(15,5) |  |  |  |  |
| 38 | `LOSSINCREASEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 39 | `LOSSINCREASETYPE6CODE` | CHAR(3) |  |  |  |  |
| 40 | `LOSSINCREASE6` | DECIMAL(15,5) |  |  |  |  |
| 41 | `LOSSINCREASEREFUOM6CODE` | CHAR(3) |  |  |  |  |
| 42 | `LOSSINCREASETYPE7CODE` | CHAR(3) |  |  |  |  |
| 43 | `LOSSINCREASE7` | DECIMAL(15,5) |  |  |  |  |
| 44 | `LOSSINCREASEREFUOM7CODE` | CHAR(3) |  |  |  |  |
| 45 | `LOSSINCREASETYPE8CODE` | CHAR(3) |  |  |  |  |
| 46 | `LOSSINCREASE8` | DECIMAL(15,5) |  |  |  |  |
| 47 | `LOSSINCREASEREFUOM8CODE` | CHAR(3) |  |  |  |  |
| 48 | `TIMETYPE1CODE` | CHAR(3) |  |  |  |  |
| 49 | `TIME1` | DECIMAL(10,5) |  |  |  |  |
| 50 | `TIMEUNIT1` | CHAR(2) |  |  |  |  |
| 51 | `TIMEREFQTY1` | DECIMAL(15,5) |  |  |  |  |
| 52 | `TIMEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 53 | `TIMETYPE2CODE` | CHAR(3) |  |  |  |  |
| 54 | `TIME2` | DECIMAL(10,5) |  |  |  |  |
| 55 | `TIMEUNIT2` | CHAR(2) |  |  |  |  |
| 56 | `TIMEREFQTY2` | DECIMAL(15,5) |  |  |  |  |
| 57 | `TIMEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 58 | `TIMETYPE3CODE` | CHAR(3) |  |  |  |  |
| 59 | `TIME3` | DECIMAL(10,5) |  |  |  |  |
| 60 | `TIMEUNIT3` | CHAR(2) |  |  |  |  |
| 61 | `TIMEREFQTY3` | DECIMAL(15,5) |  |  |  |  |
| 62 | `TIMEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 63 | `TIMETYPE4CODE` | CHAR(3) |  |  |  |  |
| 64 | `TIME4` | DECIMAL(10,5) |  |  |  |  |
| 65 | `TIMEUNIT4` | CHAR(2) |  |  |  |  |
| 66 | `TIMEREFQTY4` | DECIMAL(15,5) |  |  |  |  |
| 67 | `TIMEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 68 | `TIMETYPE5CODE` | CHAR(3) |  |  |  |  |
| 69 | `TIME5` | DECIMAL(10,5) |  |  |  |  |
| 70 | `TIMEUNIT5` | CHAR(2) |  |  |  |  |
| 71 | `TIMEREFQTY5` | DECIMAL(15,5) |  |  |  |  |
| 72 | `TIMEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 73 | `CALCULATEDTIME2` | DECIMAL(10,5) |  |  |  |  |
| 74 | `CALCULATEDTIME3` | DECIMAL(10,5) |  |  |  |  |
| 75 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTROUTESTEPBYDATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.VALIDITYDATE,
       t.ROUTEINDEX,
       t.WORKCENTERCODE,
       t.STEPNUMBER,
       t.OPERATIONCODE,
       t.WORKCENTERANDOPERATTRIBUTESCOD,
       t.PRODRESERVATIONLINKGROUPCODE
FROM   DB2ADMIN.COSTROUTESTEPBYDATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
