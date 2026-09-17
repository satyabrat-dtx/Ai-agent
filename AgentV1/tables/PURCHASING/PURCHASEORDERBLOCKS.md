# DB2ADMIN.PURCHASEORDERBLOCKS

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE`, `BLOCKSORDERTYPE`, `BLOCKSCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 2012

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `BLOCKSORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `BLOCKSCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 6 | `APPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 10 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 11 | `UNBLOCKINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 13 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 14 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 15 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 17 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BLOCKS_BLOCKS` | `PURCHASEORDERCOMPANYCODE`, `BLOCKSORDERTYPE`, `BLOCKSCODE` | [`BLOCKS`](../CORE_MASTER/BLOCKS.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `PURCHASEORDERBLOCKS.PURCHASEORDERCOMPANYCODE = BLOCKS.COMPANYCODE AND PURCHASEORDERBLOCKS.BLOCKSORDERTYPE = BLOCKS.ORDERTYPE AND PURCHASEORDERBLOCKS.BLOCKSCODE = BLOCKS.CODE` |
| `LOGREASON_LOGREASON` | `PURCHASEORDERCOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEORDERBLOCKS.PURCHASEORDERCOMPANYCODE = LOGREASON.COMPANYCODE AND PURCHASEORDERBLOCKS.LOGREASONCODE = LOGREASON.CODE` |
| `PURCHASEORDER_BLOCK` | `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE` | [`PURCHASEORDER`](../PURCHASING/PURCHASEORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PURCHASEORDERBLOCKS.PURCHASEORDERCOMPANYCODE = PURCHASEORDER.COMPANYCODE AND PURCHASEORDERBLOCKS.PURCHASEORDERCOUNTERCODE = PURCHASEORDER.COUNTERCODE AND PURCHASEORDERBLOCKS.PURCHASEORDERCODE = PURCHASEORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERBLOCKSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PURCHASEORDERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONTYPE,
       t.APPLYONCREATE,
       t.APPLYONUPDATE,
       t.APPLYONDELETE,
       t.UNBLOCKINGSEQUENCE,
       t.UNBLOCKINGTYPE
FROM   DB2ADMIN.PURCHASEORDERBLOCKS t
FETCH FIRST 100 ROWS ONLY;
```
