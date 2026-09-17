# DB2ADMIN.FINPAYMENTPROPOSAL

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 180468

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  | FK | foreign_key |  |
| 3 | `DOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `PROPOSALDATE` | DATE | NOT NULL |  |  |  |
| 6 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 7 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 8 | `GLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `GLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 10 | `CHEQUELOTCODE` | CHAR(10) |  | FK | foreign_key |  |
| 11 | `PROPOSALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `CURRENTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 13 | `COMPLETED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 15 | `FIRSTLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 16 | `FIRSTLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 17 | `SECONDLEVELAPPROVALDATE` | DATE |  |  |  |  |
| 18 | `SECONDLEVELAPPROVALUSER` | CHAR(50) |  |  |  |  |
| 19 | `COMPLETEDDATE` | DATE |  |  |  |  |
| 20 | `COMPLETEDUSER` | CHAR(50) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINPAYMENTPROPOSAL.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_DOCUMENTCURRENCY` | `DOCUMENTCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `FINPAYMENTPROPOSAL.DOCUMENTCURRENCYCODE = CURRENCY.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINPAYMENTPROPOSAL.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINPAYMENTPROPOSAL.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `FINCHEQUE_CHEQUELOT` | `COMPANYCODE`, `GLCODE`, `CHEQUELOTCODE` | [`FINCHEQUE`](../FINANCE/FINCHEQUE.md) | `COMPANYCODE`, `GLCODE`, `CODE` | RESTRICT | `FINPAYMENTPROPOSAL.COMPANYCODE = FINCHEQUE.COMPANYCODE AND FINPAYMENTPROPOSAL.GLCODE = FINCHEQUE.GLCODE AND FINPAYMENTPROPOSAL.CHEQUELOTCODE = FINCHEQUE.CODE` |
| `FINDOCUMENTTEMPLATE_DOCUMENTTEMPLATE` | `DOCUMENTTEMPLATECOMPANYCODE`, `DOCUMENTTEMPLATECODE` | [`FINDOCUMENTTEMPLATE`](../FINANCE/FINDOCUMENTTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINPAYMENTPROPOSAL.DOCUMENTTEMPLATECOMPANYCODE = FINDOCUMENTTEMPLATE.COMPANYCODE AND FINPAYMENTPROPOSAL.DOCUMENTTEMPLATECODE = FINDOCUMENTTEMPLATE.CODE` |
| `GLMASTER_GL` | `GLCOMPANYCODE`, `GLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINPAYMENTPROPOSAL.GLCOMPANYCODE = GLMASTER.COMPANYCODE AND FINPAYMENTPROPOSAL.GLCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINPAYMENTPROPOSAL_LINE` | [`FINPAYMENTPROPOSALLINE`](../FINANCE/FINPAYMENTPROPOSALLINE.md) | `FINPAYMENTPROPOSALCOMPANYCODE`, `FINPAYMENTPROPOSALCODE` | `FINPAYMENTPROPOSALLINE.FINPAYMENTPROPOSALCOMPANYCODE = FINPAYMENTPROPOSAL.COMPANYCODE AND FINPAYMENTPROPOSALLINE.FINPAYMENTPROPOSALCODE = FINPAYMENTPROPOSAL.CODE` |

## Indexes

- `FINPAYMENTPROPOSALUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.BUSINESSUNITCODE,
       t.DOCUMENTTEMPLATECOMPANYCODE,
       t.DOCUMENTTEMPLATECODE,
       t.PROPOSALDATE,
       t.DOCUMENTCURRENCYCODE,
       t.EXCHANGERATE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.CHEQUELOTCODE,
       t.PROPOSALAMOUNT
FROM   DB2ADMIN.FINPAYMENTPROPOSAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
