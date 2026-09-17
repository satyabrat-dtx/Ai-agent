# DB2ADMIN.FINCHEQUE

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `GLCODE`, `CODE`
- **FK degree**: referenced by 5 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 174438

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `GLCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `GLCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `AUTOALLOTMENT` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `FIRSTCHEQUENO` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 10 | `LASTCHEQUENO` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINCHEQUE.COMPANYCODE = COMPANY.CODE` |
| `GLMASTER_GL` | `GLCOMPANYCODE`, `GLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINCHEQUE.GLCOMPANYCODE = GLMASTER.COMPANYCODE AND FINCHEQUE.GLCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 5

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINCHEQUE_LINE` | [`FINCHEQUELINE`](../FINANCE/FINCHEQUELINE.md) | `FINCHEQUECOMPANYCODE`, `FINCHEQUEGLCODE`, `FINCHEQUECODE` | `FINCHEQUELINE.FINCHEQUECOMPANYCODE = FINCHEQUE.COMPANYCODE AND FINCHEQUELINE.FINCHEQUEGLCODE = FINCHEQUE.GLCODE AND FINCHEQUELINE.FINCHEQUECODE = FINCHEQUE.CODE` |
| `FINCHEQUE_CHEQUELOT` | [`FINDOCUMENT`](../FINANCE/FINDOCUMENT.md) | `COMPANYCODE`, `GLCODE`, `CHEQUELOTCODE` | `FINDOCUMENT.COMPANYCODE = FINCHEQUE.COMPANYCODE AND FINDOCUMENT.GLCODE = FINCHEQUE.GLCODE AND FINDOCUMENT.CHEQUELOTCODE = FINCHEQUE.CODE` |
| `FINCHEQUE_CHEQUELOT` | [`FINPAYMENTPROPOSAL`](../FINANCE/FINPAYMENTPROPOSAL.md) | `COMPANYCODE`, `GLCODE`, `CHEQUELOTCODE` | `FINPAYMENTPROPOSAL.COMPANYCODE = FINCHEQUE.COMPANYCODE AND FINPAYMENTPROPOSAL.GLCODE = FINCHEQUE.GLCODE AND FINPAYMENTPROPOSAL.CHEQUELOTCODE = FINCHEQUE.CODE` |
| `FINCHEQUE_CHEQUELOT` | [`FININTERUNITTRANSACTION`](../FINANCE/FININTERUNITTRANSACTION.md) | `COMPANYCODE`, `GLCODE`, `CHEQUELOTCODE` | `FININTERUNITTRANSACTION.COMPANYCODE = FINCHEQUE.COMPANYCODE AND FININTERUNITTRANSACTION.GLCODE = FINCHEQUE.GLCODE AND FININTERUNITTRANSACTION.CHEQUELOTCODE = FINCHEQUE.CODE` |
| `FINCHEQUE_CHEQUELOT` | [`FINPOADVANCEPROPOSAL`](../FINANCE/FINPOADVANCEPROPOSAL.md) | `COMPANYCODE`, `GLCODE`, `CHEQUELOTCODE` | `FINPOADVANCEPROPOSAL.COMPANYCODE = FINCHEQUE.COMPANYCODE AND FINPOADVANCEPROPOSAL.GLCODE = FINCHEQUE.GLCODE AND FINPOADVANCEPROPOSAL.CHEQUELOTCODE = FINCHEQUE.CODE` |

## Indexes

- `FINCHEQUEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.AUTOALLOTMENT,
       t.CURRENTSTATUS,
       t.FIRSTCHEQUENO,
       t.LASTCHEQUENO,
       t.CREATIONDATETIME
FROM   DB2ADMIN.FINCHEQUE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
