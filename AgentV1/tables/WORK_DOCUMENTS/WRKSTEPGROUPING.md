# DB2ADMIN.WRKSTEPGROUPING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 97
- **Primary key**: `COMPANYCODE`, `PRODUCTIONORDERCODE`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 22880

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODUCTIONORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 5 | `STANDARDSTEPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 6 | `STANDARDSTEPQUANTITYUOMCODE` | CHAR(3) |  |  |  |  |
| 7 | `STEPEFFICIENCYAPPLY` | CHAR(1) |  |  |  |  |
| 8 | `STEPEFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 9 | `REPETITIONNUMBER` | DECIMAL(17,6) | NOT NULL |  |  |  |
| 10 | `BATHVOLUME` | DECIMAL(17,6) |  |  |  |  |
| 11 | `BATHVOLUMEUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `LOSSINCREASETYPE1CODE` | CHAR(3) |  |  |  |  |
| 13 | `LOSSINCREASETYPE4CODE` | CHAR(3) |  |  |  |  |
| 14 | `LOSSINCREASE1` | DECIMAL(15,5) |  |  |  |  |
| 15 | `LOSSINCREASEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 16 | `LOSSINCREASETYPE2CODE` | CHAR(3) |  |  |  |  |
| 17 | `LOSSINCREASE2` | DECIMAL(15,5) |  |  |  |  |
| 18 | `LOSSINCREASEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 19 | `LOSSINCREASE3` | DECIMAL(15,5) |  |  |  |  |
| 20 | `LOSSINCREASETYPE3CODE` | CHAR(3) |  |  |  |  |
| 21 | `LOSSINCREASEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 22 | `LOSSINCREASE4` | DECIMAL(15,5) |  |  |  |  |
| 23 | `LOSSINCREASEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 24 | `LOSSINCREASETYPE5CODE` | CHAR(3) |  |  |  |  |
| 25 | `LOSSINCREASE5` | DECIMAL(15,5) |  |  |  |  |
| 26 | `LOSSINCREASEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 27 | `LOSSINCREASETYPE6CODE` | CHAR(3) |  |  |  |  |
| 28 | `LOSSINCREASE6` | DECIMAL(15,5) |  |  |  |  |
| 29 | `LOSSINCREASEREFUOM6CODE` | CHAR(3) |  |  |  |  |
| 30 | `LOSSINCREASETYPE7CODE` | CHAR(3) |  |  |  |  |
| 31 | `LOSSINCREASE7` | DECIMAL(15,5) |  |  |  |  |
| 32 | `LOSSINCREASEREFUOM7CODE` | CHAR(3) |  |  |  |  |
| 33 | `LOSSINCREASETYPE8CODE` | CHAR(3) |  |  |  |  |
| 34 | `LOSSINCREASE8` | DECIMAL(15,5) |  |  |  |  |
| 35 | `LOSSINCREASEREFUOM8CODE` | CHAR(3) |  |  |  |  |
| 36 | `PLANNINGLEADTIME` | DECIMAL(15,5) |  |  |  |  |
| 37 | `TIMETYPE1CODE` | CHAR(3) |  |  |  |  |
| 38 | `TIME1` | DECIMAL(10,5) |  |  |  |  |
| 39 | `TIMEUNIT1` | CHAR(2) |  |  |  |  |
| 40 | `TIMEREFQTY1` | DECIMAL(15,5) |  |  |  |  |
| 41 | `TIMEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 42 | `TIMETYPE2CODE` | CHAR(3) |  |  |  |  |
| 43 | `TIME2` | DECIMAL(10,5) |  |  |  |  |
| 44 | `TIMEUNIT2` | CHAR(2) |  |  |  |  |
| 45 | `TIMEREFQTY2` | DECIMAL(15,5) |  |  |  |  |
| 46 | `TIMEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 47 | `TIMETYPE3CODE` | CHAR(3) |  |  |  |  |
| 48 | `TIME3` | DECIMAL(10,5) |  |  |  |  |
| 49 | `TIMEUNIT3` | CHAR(2) |  |  |  |  |
| 50 | `TIMEREFQTY3` | DECIMAL(15,5) |  |  |  |  |
| 51 | `TIMEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 52 | `TIMETYPE4CODE` | CHAR(3) |  |  |  |  |
| 53 | `TIME4` | DECIMAL(10,5) |  |  |  |  |
| 54 | `TIMEUNIT4` | CHAR(2) |  |  |  |  |
| 55 | `TIMEREFQTY4` | DECIMAL(15,5) |  |  |  |  |
| 56 | `TIMEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 57 | `TIMETYPE5CODE` | CHAR(3) |  |  |  |  |
| 58 | `TIME5` | DECIMAL(10,5) |  |  |  |  |
| 59 | `TIMEUNIT5` | CHAR(2) |  |  |  |  |
| 60 | `TIMEREFQTY5` | DECIMAL(15,5) |  |  |  |  |
| 61 | `TIMEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 62 | `INITIALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `INITIALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `FINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `FINALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 67 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 68 | `INITIALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 69 | `INITIALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 70 | `FINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 71 | `FINALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 72 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 73 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 74 | `INITIALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `FINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 77 | `MINBEGINQUEUE` | DATE |  |  |  |  |
| 78 | `MINBEGINPRESETUP` | DATE |  |  |  |  |
| 79 | `MINBEGINOPERATION` | DATE |  |  |  |  |
| 80 | `MINBEGINPOSTSETUP` | DATE |  |  |  |  |
| 81 | `MINENDSTEP` | DATE |  |  |  |  |
| 82 | `STDBEGINQUEUE` | DATE |  |  |  |  |
| 83 | `STDBEGINPRESETUP` | DATE |  |  |  |  |
| 84 | `STDBEGINOPERATION` | DATE |  |  |  |  |
| 85 | `STDBEGINPOSTSETUP` | DATE |  |  |  |  |
| 86 | `STDENDSTEP` | DATE |  |  |  |  |
| 87 | `MAXBEGINQUEUE` | DATE |  |  |  |  |
| 88 | `MAXBEGINPRESETUP` | DATE |  |  |  |  |
| 89 | `MAXBEGINOPERATION` | DATE |  |  |  |  |
| 90 | `MAXBEGINPOSTSETUP` | DATE |  |  |  |  |
| 91 | `MAXENDSTEP` | DATE |  |  |  |  |
| 92 | `CALCULATEDTIME1` | DECIMAL(10,5) |  |  |  |  |
| 93 | `CALCULATEDTIME2` | DECIMAL(10,5) |  |  |  |  |
| 94 | `CALCULATEDTIME3` | DECIMAL(10,5) |  |  |  |  |
| 95 | `CALCULATEDTIME4` | DECIMAL(10,5) |  |  |  |  |
| 96 | `ORIGINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODUCTIONORDERCODE,
       t.LINE,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.STANDARDSTEPQUANTITY,
       t.STANDARDSTEPQUANTITYUOMCODE,
       t.STEPEFFICIENCYAPPLY,
       t.STEPEFFICIENCY,
       t.REPETITIONNUMBER,
       t.BATHVOLUME,
       t.BATHVOLUMEUOMCODE
FROM   DB2ADMIN.WRKSTEPGROUPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
