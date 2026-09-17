# DB2ADMIN.SALESORDERBLOCKS

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE`, `BLOCKSORDERTYPE`, `BLOCKSCODE`, `APPLICATIONDOCUMENTTYPE`, `APPLICATIONDOCUMENTACTIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 26500

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SALESORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `BLOCKSORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `BLOCKSCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 6 | `APPLICATIONDOCUMENTTYPE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `APPLICATIONDOCUMENTACTIONCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 8 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 12 | `UNBLOCKINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 14 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 15 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 16 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 18 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BLOCKS_BLOCKS` | `SALESORDERCOMPANYCODE`, `BLOCKSORDERTYPE`, `BLOCKSCODE` | [`BLOCKS`](../CORE_MASTER/BLOCKS.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `SALESORDERBLOCKS.SALESORDERCOMPANYCODE = BLOCKS.COMPANYCODE AND SALESORDERBLOCKS.BLOCKSORDERTYPE = BLOCKS.ORDERTYPE AND SALESORDERBLOCKS.BLOCKSCODE = BLOCKS.CODE` |
| `DOCUMENTTYPE_APPLICATIONDOCUMENT` | `BLOCKSORDERTYPE`, `APPLICATIONDOCUMENTTYPE` | [`DOCUMENTTYPE`](../CORE_MASTER/DOCUMENTTYPE.md) | `ORDERTYPE`, `TYPE` | RESTRICT | `SALESORDERBLOCKS.BLOCKSORDERTYPE = DOCUMENTTYPE.ORDERTYPE AND SALESORDERBLOCKS.APPLICATIONDOCUMENTTYPE = DOCUMENTTYPE.TYPE` |
| `LOGREASON_LOGREASON` | `SALESORDERCOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESORDERBLOCKS.SALESORDERCOMPANYCODE = LOGREASON.COMPANYCODE AND SALESORDERBLOCKS.LOGREASONCODE = LOGREASON.CODE` |
| `SALESORDER_BLOCK` | `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE` | [`SALESORDER`](../SALES/SALESORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `SALESORDERBLOCKS.SALESORDERCOMPANYCODE = SALESORDER.COMPANYCODE AND SALESORDERBLOCKS.SALESORDERCOUNTERCODE = SALESORDER.COUNTERCODE AND SALESORDERBLOCKS.SALESORDERCODE = SALESORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERBLOCKSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESORDERCOMPANYCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONDOCUMENTTYPE,
       t.APPLICATIONDOCUMENTACTIONCODE,
       t.APPLYONCREATE,
       t.APPLYONUPDATE,
       t.APPLYONDELETE,
       t.UNBLOCKINGSEQUENCE
FROM   DB2ADMIN.SALESORDERBLOCKS t
FETCH FIRST 100 ROWS ONLY;
```
