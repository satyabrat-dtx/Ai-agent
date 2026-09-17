# DB2ADMIN.USASTACCOUNTING

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `COMPANY`, `STOCKTRANSACTION`, `TRANSACTIONDETAILNUMBER`, `LINETYPE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107857

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANY` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `STOCKTRANSACTION` | CHAR(16) | NOT NULL | PK | primary_key |  |
| 2 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `DEFSTOCKTRNTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `DEFACCTEMPLATETEMPLATECODE` | CHAR(6) |  |  |  |  |
| 5 | `DEFITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `DEFSUBCODE01` | CHAR(20) |  |  |  |  |
| 7 | `DEFSUBCODE02` | CHAR(10) |  |  |  |  |
| 8 | `DEFSUBCODE03` | CHAR(10) |  |  |  |  |
| 9 | `DEFSUBCODE04` | CHAR(10) |  |  |  |  |
| 10 | `DEFSUBCODE05` | CHAR(10) |  |  |  |  |
| 11 | `DEFSUBCODE06` | CHAR(10) |  |  |  |  |
| 12 | `DEFSUBCODE07` | CHAR(10) |  |  |  |  |
| 13 | `DEFSUBCODE08` | CHAR(10) |  |  |  |  |
| 14 | `DEFSUBCODE09` | CHAR(10) |  |  |  |  |
| 15 | `DEFSUBCODE10` | CHAR(10) |  |  |  |  |
| 16 | `DEFLOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 17 | `DEFARTICLEGROUPCODE` | CHAR(10) |  |  |  |  |
| 18 | `DEFQUALITYLEVEL` | DECIMAL(2,0) |  |  |  |  |
| 19 | `DEFORDERTEMPLATE` | CHAR(3) |  |  |  |  |
| 20 | `DEFCUSTOMERSUPPLIER` | CHAR(8) |  |  |  |  |
| 21 | `DEFCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 22 | `DEFCOSTCENTERGROUPGROUPCODE` | CHAR(3) |  |  |  |  |
| 23 | `ACCOUNTTRANSACTIONNUMBER` | CHAR(16) | NOT NULL |  |  |  |
| 24 | `ACCOUNTCODE` | CHAR(20) | NOT NULL |  |  |  |
| 25 | `UNITVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 26 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 28 | `LINETYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 29 | `DOCUMENTCLASS` | CHAR(2) |  |  |  |  |
| 30 | `ACCOUNTINGTYPE` | CHAR(2) |  |  |  |  |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USASTACCOUNTINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANY,
       t.STOCKTRANSACTION,
       t.TRANSACTIONDETAILNUMBER,
       t.DEFSTOCKTRNTEMPLATECODE,
       t.DEFACCTEMPLATETEMPLATECODE,
       t.DEFITEMTYPECODE,
       t.DEFSUBCODE01,
       t.DEFSUBCODE02,
       t.DEFSUBCODE03,
       t.DEFSUBCODE04,
       t.DEFSUBCODE05,
       t.DEFSUBCODE06
FROM   DB2ADMIN.USASTACCOUNTING t
FETCH FIRST 100 ROWS ONLY;
```
