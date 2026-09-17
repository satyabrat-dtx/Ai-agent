# DB2ADMIN.USAACCOUNTINGJOURNAL

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 36
- **Primary key**: `COMPANYCODE`, `TRANSACTIONNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107455

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TRANSACTIONNUMBER` | CHAR(16) | NOT NULL | PK | primary_key |  |
| 2 | `DOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 3 | `JOURNALNUM` | CHAR(10) |  |  |  |  |
| 4 | `ACCOUNTTYPE` | CHAR(1) |  |  |  |  |
| 5 | `ACCOUNTNUM` | CHAR(15) |  |  |  |  |
| 6 | `TXD` | CHAR(30) |  |  |  |  |
| 7 | `AMOUNTCURDEBIT` | DECIMAL(17,2) |  |  |  |  |
| 8 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 9 | `EXCHRATE` | DECIMAL(5,0) |  |  |  |  |
| 10 | `COSTCENTER` | CHAR(20) |  |  |  |  |
| 11 | `FINANCIALPARCODE` | CHAR(15) |  |  |  |  |
| 12 | `VOUCHER` | CHAR(12) |  |  |  |  |
| 13 | `AMOUNTCURCREDIT` | DECIMAL(17,2) |  |  |  |  |
| 14 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 15 | `INVOICE` | CHAR(15) |  |  |  |  |
| 16 | `DOCUMENTNUMBER` | CHAR(15) |  |  |  |  |
| 17 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 18 | `PAYMODE` | CHAR(5) |  |  |  |  |
| 19 | `DUEDATE` | DATE |  |  |  |  |
| 20 | `TAXGROUP` | CHAR(50) |  |  |  |  |
| 21 | `TAXITEMGROUP` | CHAR(10) |  |  |  |  |
| 22 | `POSTINGPROFILE` | CHAR(10) |  |  |  |  |
| 23 | `ACCOUNTTYPEOFFSET` | CHAR(1) |  |  |  |  |
| 24 | `ACCOUNTNUMOFFSET` | CHAR(15) |  |  |  |  |
| 25 | `DOCUMENTCLASS` | CHAR(2) |  |  |  |  |
| 26 | `ACCOUNTINGTYPE` | CHAR(2) |  |  |  |  |
| 27 | `PERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 28 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 29 | `ACKDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `ACKUSER` | CHAR(25) |  |  |  |  |
| 31 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 32 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 33 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 34 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USAACCOUNTINGJOURNAL.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USAACCOUNTINGJOURNALUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TRANSACTIONNUMBER,
       t.DOCUMENTTYPE,
       t.JOURNALNUM,
       t.ACCOUNTTYPE,
       t.ACCOUNTNUM,
       t.TXD,
       t.AMOUNTCURDEBIT,
       t.CURRENCYCODE,
       t.EXCHRATE,
       t.COSTCENTER,
       t.FINANCIALPARCODE
FROM   DB2ADMIN.USAACCOUNTINGJOURNAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
