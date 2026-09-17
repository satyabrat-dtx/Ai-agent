# DB2ADMIN.QUALITYDOCUMENTEXP

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPHEADERCODE`, `EXPHEADERSUBGROUPCODE`, `EXPHEADERNUMBERID`, `EXPITEMTYPEAFICODE`, `EXPSUBCODE01`, `EXPSUBCODE02`, `EXPSUBCODE03`, `EXPSUBCODE04`, `EXPSUBCODE05`, `EXPSUBCODE06`, `EXPSUBCODE07`, `EXPSUBCODE08`, `EXPSUBCODE09`, `EXPSUBCODE10`, `EXPLOTCODE`, `EXPITEMELEMENTSUBCODEKEY`, `EXPITEMELEMENTCODE`, `EXPDEMANDCOUNTERCODE`, `EXPDEMANDCODE`, `EXPPRODUCTIONORDERCODE`, `EXPORDERPARTNERREQUIRED`, `EXPORDPRNCSMSUPCSMSUPCODE`, `EXPHEADERLINE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117360

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPHEADERCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 3 | `EXPHEADERSUBGROUPCODE` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 4 | `EXPHEADERNUMBERID` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `EXPITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `EXPSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 7 | `EXPSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `EXPSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `EXPSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `EXPSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `EXPSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `EXPSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `EXPSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `EXPSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `EXPSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 16 | `EXPLOTCODE` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 17 | `EXPITEMELEMENTSUBCODEKEY` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 18 | `EXPITEMELEMENTCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 19 | `EXPDEMANDCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 20 | `EXPDEMANDCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 21 | `EXPPRODUCTIONORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 22 | `EXPORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 23 | `EXPORDPRNCSMSUPCSMSUPCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 24 | `EXPHEADERLINE` | DECIMAL(15,0) | NOT NULL | PK | primary_key |  |
| 25 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 26 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 27 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 28 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 29 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QUALITYDOCUMENTEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPHEADERCODE,
       t.EXPHEADERSUBGROUPCODE,
       t.EXPHEADERNUMBERID,
       t.EXPITEMTYPEAFICODE,
       t.EXPSUBCODE01,
       t.EXPSUBCODE02,
       t.EXPSUBCODE03,
       t.EXPSUBCODE04,
       t.EXPSUBCODE05,
       t.EXPSUBCODE06
FROM   DB2ADMIN.QUALITYDOCUMENTEXP t
FETCH FIRST 100 ROWS ONLY;
```
