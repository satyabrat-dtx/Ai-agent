# DB2ADMIN.PURPREPAYMENTLINEACCTRANSUSED

- **Module**: `PURCHASING` (medium confidence — table name starts with 'PUR')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `SUPPLIERTYPE`, `SUPPLIERCODE`, `PREPAYMENTNUMBER`, `PREPAYMENTLINENUMBER`, `ACCOUNTTRANSACTIONNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237870

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SUPPLIERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SUPPLIERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PREPAYMENTNUMBER` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PREPAYMENTLINENUMBER` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `LINEUSEDAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 6 | `ACCOUNTTRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PURCHASEPREPAYMENTLINE_ACCTRANSUSED` | `COMPANYCODE`, `SUPPLIERTYPE`, `SUPPLIERCODE`, `PREPAYMENTNUMBER`, `PREPAYMENTLINENUMBER` | [`PURCHASEPREPAYMENTLINE`](../PURCHASING/PURCHASEPREPAYMENTLINE.md) | `PURCHASEPREPAYMENTCOMPANYCODE`, `PURPREPAYMENTSUPCSMSUPTYPE`, `PURPREPAYMENTSUPCSMSUPCODE`, `PURPREPAYMENTPREPAYMENTNUMBER`, `LINENUMBER` | RESTRICT | `PURPREPAYMENTLINEACCTRANSUSED.COMPANYCODE = PURCHASEPREPAYMENTLINE.PURCHASEPREPAYMENTCOMPANYCODE AND PURPREPAYMENTLINEACCTRANSUSED.SUPPLIERTYPE = PURCHASEPREPAYMENTLINE.PURPREPAYMENTSUPCSMSUPTYPE AND PURPREPAYMENTLINEACCTRANSUSED.SUPPLIERCODE = PURCHASEPREPAYMENTLINE.PURPREPAYMENTSUPCSMSUPCODE AND PURPREPAYMENTLINEACCTRANSUSED.PREPAYMENTNUMBER = PURCHASEPREPAYMENTLINE.PURPREPAYMENTPREPAYMENTNUMBER AND PURPREPAYMENTLINEACCTRANSUSED.PREPAYMENTLINENUMBER = PURCHASEPREPAYMENTLINE.LINENUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PREPAYMENTLINEACCTRANSUSEDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SUPPLIERTYPE,
       t.SUPPLIERCODE,
       t.PREPAYMENTNUMBER,
       t.PREPAYMENTLINENUMBER,
       t.LINEUSEDAMOUNT,
       t.ACCOUNTTRANSACTIONNUMBER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PURPREPAYMENTLINEACCTRANSUSED t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
