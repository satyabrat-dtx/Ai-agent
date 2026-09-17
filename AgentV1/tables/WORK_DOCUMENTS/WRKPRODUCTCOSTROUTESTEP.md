# DB2ADMIN.WRKPRODUCTCOSTROUTESTEP

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 81
- **Primary key**: `UNIQUEID`, `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 7317

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 4 | `PLANTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 5 | `COSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `ROUTEINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 8 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 9 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `OPERATIONCODE` | CHAR(8) | NOT NULL |  |  |  |
| 11 | `WORKCENTERANDOPERATTRIBUTESCOD` | CHAR(20) |  |  |  |  |
| 12 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 13 | `RUNNINGDATE` | DATE |  |  |  |  |
| 14 | `EFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 15 | `EFFICIENCYAPPLY` | CHAR(1) |  |  |  |  |
| 16 | `STDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `STDUOMCODE` | CHAR(3) |  |  |  |  |
| 18 | `REPETITIONNUMBER` | DECIMAL(15,5) |  |  |  |  |
| 19 | `INITQTYPRIMEUOM` | DECIMAL(20,10) |  |  |  |  |
| 20 | `FINALQTYPRIMEUOM` | DECIMAL(20,10) |  |  |  |  |
| 21 | `INITQTYSECONDUOM` | DECIMAL(20,10) |  |  |  |  |
| 22 | `FINALQTYSECONDUOM` | DECIMAL(20,10) |  |  |  |  |
| 23 | `WASTEQTYINPRIMARYUOM` | DECIMAL(20,10) |  |  |  |  |
| 24 | `WASTEQTYINSECONDARYUOM` | DECIMAL(20,10) |  |  |  |  |
| 25 | `TOTALTIME` | DECIMAL(20,10) |  |  |  |  |
| 26 | `ENDCALCULATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 29 | `LOSSINCREASETYPE1CODE` | CHAR(3) |  |  |  |  |
| 30 | `LOSSINCREASE1` | DECIMAL(15,5) |  |  |  |  |
| 31 | `LOSSINCREASEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 32 | `LOSSINCREASETYPE2CODE` | CHAR(3) |  |  |  |  |
| 33 | `LOSSINCREASE2` | DECIMAL(15,5) |  |  |  |  |
| 34 | `LOSSINCREASEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 35 | `LOSSINCREASETYPE3CODE` | CHAR(3) |  |  |  |  |
| 36 | `LOSSINCREASE3` | DECIMAL(15,5) |  |  |  |  |
| 37 | `LOSSINCREASEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 38 | `LOSSINCREASETYPE4CODE` | CHAR(3) |  |  |  |  |
| 39 | `LOSSINCREASE4` | DECIMAL(15,5) |  |  |  |  |
| 40 | `LOSSINCREASEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 41 | `LOSSINCREASETYPE5CODE` | CHAR(3) |  |  |  |  |
| 42 | `LOSSINCREASE5` | DECIMAL(15,5) |  |  |  |  |
| 43 | `LOSSINCREASEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 44 | `LOSSINCREASETYPE6CODE` | CHAR(3) |  |  |  |  |
| 45 | `LOSSINCREASE6` | DECIMAL(15,5) |  |  |  |  |
| 46 | `LOSSINCREASEREFUOM6CODE` | CHAR(3) |  |  |  |  |
| 47 | `LOSSINCREASETYPE7CODE` | CHAR(3) |  |  |  |  |
| 48 | `LOSSINCREASE7` | DECIMAL(15,5) |  |  |  |  |
| 49 | `LOSSINCREASEREFUOM7CODE` | CHAR(3) |  |  |  |  |
| 50 | `LOSSINCREASETYPE8CODE` | CHAR(3) |  |  |  |  |
| 51 | `LOSSINCREASE8` | DECIMAL(15,5) |  |  |  |  |
| 52 | `LOSSINCREASEREFUOM8CODE` | CHAR(3) |  |  |  |  |
| 53 | `TIMETYPE1CODE` | CHAR(3) |  |  |  |  |
| 54 | `TIME1` | DECIMAL(10,5) |  |  |  |  |
| 55 | `TIMEUNIT1` | CHAR(2) |  |  |  |  |
| 56 | `TIMEREFQTY1` | DECIMAL(15,5) |  |  |  |  |
| 57 | `TIMEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 58 | `TIMETYPE2CODE` | CHAR(3) |  |  |  |  |
| 59 | `TIME2` | DECIMAL(10,5) |  |  |  |  |
| 60 | `TIMEUNIT2` | CHAR(2) |  |  |  |  |
| 61 | `TIMEREFQTY2` | DECIMAL(15,5) |  |  |  |  |
| 62 | `TIMEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 63 | `TIMETYPE3CODE` | CHAR(3) |  |  |  |  |
| 64 | `TIME3` | DECIMAL(10,5) |  |  |  |  |
| 65 | `TIMEUNIT3` | CHAR(2) |  |  |  |  |
| 66 | `TIMEREFQTY3` | DECIMAL(15,5) |  |  |  |  |
| 67 | `TIMEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 68 | `TIMETYPE4CODE` | CHAR(3) |  |  |  |  |
| 69 | `TIME4` | DECIMAL(10,5) |  |  |  |  |
| 70 | `TIMEUNIT4` | CHAR(2) |  |  |  |  |
| 71 | `TIMEREFQTY4` | DECIMAL(15,5) |  |  |  |  |
| 72 | `TIMEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 73 | `TIMETYPE5CODE` | CHAR(3) |  |  |  |  |
| 74 | `TIME5` | DECIMAL(10,5) |  |  |  |  |
| 75 | `TIMEUNIT5` | CHAR(2) |  |  |  |  |
| 76 | `TIMEREFQTY5` | DECIMAL(15,5) |  |  |  |  |
| 77 | `TIMEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 78 | `SUBUNIQUEID` | INTEGER | NOT NULL |  |  |  |
| 79 | `CALCULATEDTIME2` | DECIMAL(10,5) |  |  |  |  |
| 80 | `CALCULATEDTIME3` | DECIMAL(10,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPRDCSTRTESTEP01` (UNIQUEID, PLANTCODE, COSTGROUPCODE, COSTSCOSTGROUPCODE, PRODUCTINDEX)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.TABLEINDEX,
       t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.ROUTEINDEX,
       t.STEPNUMBER,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.WORKCENTERANDOPERATTRIBUTESCOD
FROM   DB2ADMIN.WRKPRODUCTCOSTROUTESTEP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
