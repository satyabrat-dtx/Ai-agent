# DB2ADMIN.GMTCARTONDETAILTRANSACTION31102024

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `no_primary_key`
- **Columns**: 9
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216854

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GMTCRTDLTGMTCRTHDRCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `GMTCRTDLTGMTCRTHEADERNUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 2 | `GARMENTCARTONDETAILCARTONCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 4 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `GMTCRTDLTCARTONITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `GMTCRTDETAILCARTONSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 8 | `CARTONTRANSACTIONTYPE` | CHAR(2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.GMTCRTDLTGMTCRTHDRCOMPANYCODE,
       t.GMTCRTDLTGMTCRTHEADERNUMBERID,
       t.GARMENTCARTONDETAILCARTONCODE,
       t.TRANSACTIONNUMBER,
       t.STATUS,
       t.ABSUNIQUEID,
       t.GMTCRTDLTCARTONITEMTYPECODE,
       t.GMTCRTDETAILCARTONSUBCODE01,
       t.CARTONTRANSACTIONTYPE
FROM   DB2ADMIN.GMTCARTONDETAILTRANSACTION31102024 t
FETCH FIRST 100 ROWS ONLY;
```
