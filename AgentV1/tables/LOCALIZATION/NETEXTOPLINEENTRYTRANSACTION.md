# DB2ADMIN.NETEXTOPLINEENTRYTRANSACTION

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `EXTOPLINECOMPANYCODE`, `EXTOPLINECOUNTERCODE`, `EXTOPLINECODE`, `EXTOPLINEORDERLINE`, `STOCKTRNTRANSACTIONNUMBER`, `STOCKTRNTRNDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 221455

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `EXTOPLINECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `EXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 4 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `MRNHEADERDIVISIONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `MRNHEADERMRNPREFIXCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `MRNHEADERCODE` | DECIMAL(11,0) |  | FK | foreign_key |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `MRNHEADER_MRNHEADER` | `EXTOPLINECOMPANYCODE`, `MRNHEADERDIVISIONCODE`, `MRNHEADERMRNPREFIXCODE`, `MRNHEADERCODE` | [`MRNHEADER`](../CORE_MASTER/MRNHEADER.md) | `COMPANYCODE`, `DIVISIONCODE`, `MRNPREFIXCODE`, `CODE` | RESTRICT | `NETEXTOPLINEENTRYTRANSACTION.EXTOPLINECOMPANYCODE = MRNHEADER.COMPANYCODE AND NETEXTOPLINEENTRYTRANSACTION.MRNHEADERDIVISIONCODE = MRNHEADER.DIVISIONCODE AND NETEXTOPLINEENTRYTRANSACTION.MRNHEADERMRNPREFIXCODE = MRNHEADER.MRNPREFIXCODE AND NETEXTOPLINEENTRYTRANSACTION.MRNHEADERCODE = MRNHEADER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETEXTOPLINEETRANSACTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EXTOPLINECOMPANYCODE,
       t.EXTOPLINECOUNTERCODE,
       t.EXTOPLINECODE,
       t.EXTOPLINEORDERLINE,
       t.STOCKTRNTRANSACTIONNUMBER,
       t.STOCKTRNTRNDETAILNUMBER,
       t.MRNHEADERDIVISIONCODE,
       t.MRNHEADERMRNPREFIXCODE,
       t.MRNHEADERCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.NETEXTOPLINEENTRYTRANSACTION t
FETCH FIRST 100 ROWS ONLY;
```
