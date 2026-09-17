# DB2ADMIN.GARMENTCARTONDETAIL31102024

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `no_primary_key`
- **Columns**: 21
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216819

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GARMENTCARTONHEADERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `GARMENTCARTONHEADERNUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 2 | `CARTONCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `SALESORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `SALESORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `PACKINGGROUP` | CHAR(15) |  |  |  |  |
| 6 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 7 | `SHIPPINGSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `CARTONCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 16 | `CARTONITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 17 | `CARTONSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 18 | `ENTRYTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 19 | `ENTRYTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `ENTRYTEMPLATECODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.GARMENTCARTONHEADERCOMPANYCODE,
       t.GARMENTCARTONHEADERNUMBERID,
       t.CARTONCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.PACKINGGROUP,
       t.QUANTITY,
       t.SHIPPINGSTATUS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.GARMENTCARTONDETAIL31102024 t
FETCH FIRST 100 ROWS ONLY;
```
