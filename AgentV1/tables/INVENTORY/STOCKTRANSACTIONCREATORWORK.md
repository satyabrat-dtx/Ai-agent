# DB2ADMIN.STOCKTRANSACTIONCREATORWORK

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `business_data`
- **Columns**: 39
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 6877

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ELEMENTVIEWDECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 5 | `ELEMENTVIEWDECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 6 | `ELEMENTVIEWDECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 7 | `ELEMENTVIEWDECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 8 | `ELEMENTVIEWDECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 9 | `ELEMENTVIEWDECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 10 | `ELEMENTVIEWDECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 11 | `ELEMENTVIEWDECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 12 | `ELEMENTVIEWDECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 13 | `ELEMENTVIEWDECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 14 | `ELEMENTVIEWLOTCODE` | CHAR(35) |  |  |  |  |
| 15 | `ELMVIEWCONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `ELEMENTVIEWCONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 17 | `ELMVIEWCONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 18 | `ELMVIEWPHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 19 | `ELMVIEWWHSLOCWHSZONECODE` | CHAR(3) |  |  |  |  |
| 20 | `ELMVIEWWAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 21 | `ELEMENTVIEWITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 22 | `ELEMENTVIEWSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 23 | `ELEMENTVIEWCODE` | CHAR(15) |  |  |  |  |
| 24 | `LOTVIEWITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 25 | `LOTVIEWDECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 26 | `LOTVIEWDECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 27 | `LOTVIEWDECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 28 | `LOTVIEWDECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 29 | `LOTVIEWDECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 30 | `LOTVIEWDECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 31 | `LOTVIEWDECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 32 | `LOTVIEWDECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 33 | `LOTVIEWDECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 34 | `LOTVIEWDECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 35 | `LOTVIEWCODE` | CHAR(35) |  |  |  |  |
| 36 | `BALANCEVIEWNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 37 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 38 | `LOTVIEWCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STOCKTRNCREATORWORKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.ELEMENTVIEWDECOSUBCODE01,
       t.ELEMENTVIEWDECOSUBCODE02,
       t.ELEMENTVIEWDECOSUBCODE03,
       t.ELEMENTVIEWDECOSUBCODE04,
       t.ELEMENTVIEWDECOSUBCODE05,
       t.ELEMENTVIEWDECOSUBCODE06,
       t.ELEMENTVIEWDECOSUBCODE07,
       t.ELEMENTVIEWDECOSUBCODE08
FROM   DB2ADMIN.STOCKTRANSACTIONCREATORWORK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
