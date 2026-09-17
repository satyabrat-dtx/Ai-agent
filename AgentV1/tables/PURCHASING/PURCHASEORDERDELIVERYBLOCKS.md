# DB2ADMIN.PURCHASEORDERDELIVERYBLOCKS

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `ORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `PURORDERDELIVERYDELIVERYLINE`, `BLOCKSORDERTYPE`, `BLOCKSCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 22344

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PURORDERDELIVERYDELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `BLOCKSORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `BLOCKSCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 9 | `APPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 13 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 14 | `UNBLOCKINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 15 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 16 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 17 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 18 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BLOCKS_BLOCKS` | `COMPANYCODE`, `BLOCKSORDERTYPE`, `BLOCKSCODE` | [`BLOCKS`](../CORE_MASTER/BLOCKS.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `PURCHASEORDERDELIVERYBLOCKS.COMPANYCODE = BLOCKS.COMPANYCODE AND PURCHASEORDERDELIVERYBLOCKS.BLOCKSORDERTYPE = BLOCKS.ORDERTYPE AND PURCHASEORDERDELIVERYBLOCKS.BLOCKSCODE = BLOCKS.CODE` |
| `LOGREASON_LOGREASON` | `COMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEORDERDELIVERYBLOCKS.COMPANYCODE = LOGREASON.COMPANYCODE AND PURCHASEORDERDELIVERYBLOCKS.LOGREASONCODE = LOGREASON.CODE` |
| `PURCHASEORDERDELIVERY_BLOCK` | `COMPANYCODE`, `COUNTERCODE`, `ORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `PURORDERDELIVERYDELIVERYLINE` | [`PURCHASEORDERDELIVERY`](../PURCHASING/PURCHASEORDERDELIVERY.md) | `PURORDLINEPURORDERCOMPANYCODE`, `PURORDLINEPURORDERCOUNTERCODE`, `PURORDERLINEPURCHASEORDERCODE`, `PURCHASEORDERLINEORDERLINE`, `PURCHASEORDERLINEORDERSUBLINE`, `DELIVERYLINE` | RESTRICT | `PURCHASEORDERDELIVERYBLOCKS.COMPANYCODE = PURCHASEORDERDELIVERY.PURORDLINEPURORDERCOMPANYCODE AND PURCHASEORDERDELIVERYBLOCKS.COUNTERCODE = PURCHASEORDERDELIVERY.PURORDLINEPURORDERCOUNTERCODE AND PURCHASEORDERDELIVERYBLOCKS.ORDERCODE = PURCHASEORDERDELIVERY.PURORDERLINEPURCHASEORDERCODE AND PURCHASEORDERDELIVERYBLOCKS.ORDERLINE = PURCHASEORDERDELIVERY.PURCHASEORDERLINEORDERLINE AND PURCHASEORDERDELIVERYBLOCKS.ORDERSUBLINE = PURCHASEORDERDELIVERY.PURCHASEORDERLINEORDERSUBLINE AND PURCHASEORDERDELIVERYBLOCKS.PURORDERDELIVERYDELIVERYLINE = PURCHASEORDERDELIVERY.DELIVERYLINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURORDERDELIVERYBLOCKSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.ORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.PURORDERDELIVERYDELIVERYLINE,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONTYPE,
       t.APPLYONCREATE,
       t.APPLYONUPDATE
FROM   DB2ADMIN.PURCHASEORDERDELIVERYBLOCKS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
