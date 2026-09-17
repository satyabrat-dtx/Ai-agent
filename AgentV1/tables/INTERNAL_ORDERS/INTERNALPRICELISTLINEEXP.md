# DB2ADMIN.INTERNALPRICELISTLINEEXP

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `ENVIRONMENTCODE`, `EXPINTPRCDTLINTPRCLISTCMYCODE`, `EXPINTPRCLISTDLTINTPRCLISTCOD`, `EXPINTPRCLISTDLTCOSTGROUPCODE`, `EXPINTPRCLISTDLTITEMTYPECODE`, `EXPINTPRCLISTDETAILPLANTCODE`, `EXPSUBCODE01`, `EXPSUBCODE02`, `EXPSUBCODE03`, `EXPSUBCODE04`, `EXPSUBCODE05`, `EXPSUBCODE06`, `EXPSUBCODE07`, `EXPSUBCODE08`, `EXPSUBCODE09`, `EXPSUBCODE10`, `EXPVALIDFROMDATE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 90362

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPINTPRCDTLINTPRCLISTCMYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPINTPRCLISTDLTINTPRCLISTCOD` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPINTPRCLISTDLTCOSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `EXPINTPRCLISTDLTITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `EXPINTPRCLISTDETAILPLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
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
| 16 | `EXPVALIDFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 17 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 18 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 19 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 22 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INTERNALPRICELISTLINEEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPINTPRCDTLINTPRCLISTCMYCODE,
       t.EXPINTPRCLISTDLTINTPRCLISTCOD,
       t.EXPINTPRCLISTDLTCOSTGROUPCODE,
       t.EXPINTPRCLISTDLTITEMTYPECODE,
       t.EXPINTPRCLISTDETAILPLANTCODE,
       t.EXPSUBCODE01,
       t.EXPSUBCODE02,
       t.EXPSUBCODE03,
       t.EXPSUBCODE04,
       t.EXPSUBCODE05,
       t.EXPSUBCODE06
FROM   DB2ADMIN.INTERNALPRICELISTLINEEXP t
FETCH FIRST 100 ROWS ONLY;
```
