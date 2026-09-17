# DB2ADMIN.QASTANDARDPARAMETEREXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPDIVISIONCODE`, `EXPDFTITEMTYPECODE`, `EXPSUBCODE01`, `EXPSUBCODE02`, `EXPSUBCODE03`, `EXPSUBCODE04`, `EXPSUBCODE05`, `EXPSUBCODE06`, `EXPSUBCODE07`, `EXPSUBCODE08`, `EXPSUBCODE09`, `EXPSUBCODE10`, `EXPGCDGRPUSERGENGROUPTYPECODE`, `EXPGCDGROUPCODE`, `EXPGCDCSMCUSTOMERSUPPLIERTYPE`, `EXPGCDCSMCUSTOMERSUPPLIERCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89673

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 3 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 4 | `EXPDIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `EXPDFTITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
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
| 16 | `EXPGCDGRPUSERGENGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 17 | `EXPGCDGROUPCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 18 | `EXPGCDCSMCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 19 | `EXPGCDCSMCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 20 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QASTANDARDPARAMETEREXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.EXPDIVISIONCODE,
       t.EXPDFTITEMTYPECODE,
       t.EXPSUBCODE01,
       t.EXPSUBCODE02,
       t.EXPSUBCODE03,
       t.EXPSUBCODE04,
       t.EXPSUBCODE05,
       t.EXPSUBCODE06
FROM   DB2ADMIN.QASTANDARDPARAMETEREXP t
FETCH FIRST 100 ROWS ONLY;
```
