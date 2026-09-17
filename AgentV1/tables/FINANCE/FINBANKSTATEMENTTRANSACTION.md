# DB2ADMIN.FINBANKSTATEMENTTRANSACTION

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `BANKGLCODE`, `SERIALNO`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 179054

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `BANKGLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `BANKGLCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `SERIALNO` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `FINMONTH` | INTEGER | NOT NULL |  |  |  |
| 6 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 7 | `NARRATION` | VARCHAR(255) |  |  |  |  |
| 8 | `CHEQUENO` | CHAR(15) |  |  |  |  |
| 9 | `CREDIT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `DEBIT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `RECONCILATIONTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 12 | `BANKBALANCE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `UTRNO` | VARCHAR(100) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINBANKSTATEMENTTRANSACTION.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINBANKSTATEMENTTRANSACTION_FBSTATETRAN` | [`FINRECONCILIATIONTRANSACTION`](../FINANCE/FINRECONCILIATIONTRANSACTION.md) | `COMPANYCODE`, `FBSTATETRANBUSINESSUNITCODE`, `FBSTATETRANBANKGLCODE`, `FBSTATETRANSERIALNO` | `FINRECONCILIATIONTRANSACTION.COMPANYCODE = FINBANKSTATEMENTTRANSACTION.COMPANYCODE AND FINRECONCILIATIONTRANSACTION.FBSTATETRANBUSINESSUNITCODE = FINBANKSTATEMENTTRANSACTION.BUSINESSUNITCODE AND FINRECONCILIATIONTRANSACTION.FBSTATETRANBANKGLCODE = FINBANKSTATEMENTTRANSACTION.BANKGLCODE AND FINRECONCILIATIONTRANSACTION.FBSTATETRANSERIALNO = FINBANKSTATEMENTTRANSACTION.SERIALNO` |

## Indexes

- `FINBANKSTATEMENTTRNUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.SERIALNO,
       t.FINMONTH,
       t.TRANSACTIONDATE,
       t.NARRATION,
       t.CHEQUENO,
       t.CREDIT,
       t.DEBIT,
       t.RECONCILATIONTRANSACTIONNUMBER
FROM   DB2ADMIN.FINBANKSTATEMENTTRANSACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
