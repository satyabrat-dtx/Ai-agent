# DB2ADMIN.WRKFINBANKRECONCILESUMMARY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `COMPANYCODE`, `LINENO`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181244

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `ASONDATE` | DATE |  |  |  |  |
| 4 | `BANKGL` | CHAR(15) |  |  |  |  |
| 5 | `GLDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 6 | `LEDGERTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 7 | `LEDGERCREDITAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `LEDGERDEBITAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `BANKTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `BANKCREDITAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `BANKDEBITAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 13 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 14 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 15 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 16 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 17 | `FINDOCUMENTLINENO` | DECIMAL(7,0) |  |  |  |  |
| 18 | `POSTINGDATE` | DATE |  |  |  |  |
| 19 | `CHEQUENO` | CHAR(20) |  |  |  |  |
| 20 | `CHEQUEDATE` | DATE |  |  |  |  |
| 21 | `NARRATION` | VARCHAR(255) |  |  |  |  |
| 22 | `CREDITDOC` | DECIMAL(18,5) |  |  |  |  |
| 23 | `DEBITDOC` | DECIMAL(18,5) |  |  |  |  |
| 24 | `SELECTLEDGER` | SMALLINT | NOT NULL |  |  |  |
| 25 | `FINTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 26 | `LEDGERREMARK` | VARCHAR(255) |  |  |  |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINBANKRECONCILESUMMARYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LINENO,
       t.CREATIONTIMESTAMP,
       t.ASONDATE,
       t.BANKGL,
       t.GLDESCRIPTION,
       t.LEDGERTOTALAMOUNT,
       t.LEDGERCREDITAMOUNT,
       t.LEDGERDEBITAMOUNT,
       t.BANKTOTALAMOUNT,
       t.BANKCREDITAMOUNT,
       t.BANKDEBITAMOUNT
FROM   DB2ADMIN.WRKFINBANKRECONCILESUMMARY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
