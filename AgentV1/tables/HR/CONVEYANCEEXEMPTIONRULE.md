# DB2ADMIN.CONVEYANCEEXEMPTIONRULE

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `FINANCIALYEARCODE`, `GROUPCODE`, `ITEMCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 150610

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FINANCIALYEARCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `GROUPCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITEMCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PAYELEMENTTYPE` | CHAR(1) | NOT NULL | FK | foreign_key |  |
| 5 | `PAYELEMENTCODE` | CHAR(6) |  | FK | foreign_key |  |
| 6 | `MAXAMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 7 | `MAXAMOUNTDISABILITY` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CONVEYANCEEXEMPTIONRULE.COMPANYCODE = COMPANY.CODE` |
| `GROUPITEM_ITEM` | `COMPANYCODE`, `FINANCIALYEARCODE`, `GROUPCODE`, `ITEMCODE` | [`GROUPITEM`](../HR/GROUPITEM.md) | `INVESTMENTGROUPCOMPANYCODE`, `INVESTMENTGRPFINANCIALYEARCOD`, `INVESTMENTGROUPCODE`, `CODE` | RESTRICT | `CONVEYANCEEXEMPTIONRULE.COMPANYCODE = GROUPITEM.INVESTMENTGROUPCOMPANYCODE AND CONVEYANCEEXEMPTIONRULE.FINANCIALYEARCODE = GROUPITEM.INVESTMENTGRPFINANCIALYEARCOD AND CONVEYANCEEXEMPTIONRULE.GROUPCODE = GROUPITEM.INVESTMENTGROUPCODE AND CONVEYANCEEXEMPTIONRULE.ITEMCODE = GROUPITEM.CODE` |
| `INVESTMENTGROUP_GROUP` | `COMPANYCODE`, `FINANCIALYEARCODE`, `GROUPCODE` | [`INVESTMENTGROUP`](../HR/INVESTMENTGROUP.md) | `COMPANYCODE`, `FINANCIALYEARCODE`, `CODE` | RESTRICT | `CONVEYANCEEXEMPTIONRULE.COMPANYCODE = INVESTMENTGROUP.COMPANYCODE AND CONVEYANCEEXEMPTIONRULE.FINANCIALYEARCODE = INVESTMENTGROUP.FINANCIALYEARCODE AND CONVEYANCEEXEMPTIONRULE.GROUPCODE = INVESTMENTGROUP.CODE` |
| `PAYELEMENT_PAYELEMENT` | `COMPANYCODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE` | [`PAYELEMENT`](../CORE_MASTER/PAYELEMENT.md) | `COMPANYCODE`, `PAYELEMENTTYPE`, `CODE` | RESTRICT | `CONVEYANCEEXEMPTIONRULE.COMPANYCODE = PAYELEMENT.COMPANYCODE AND CONVEYANCEEXEMPTIONRULE.PAYELEMENTTYPE = PAYELEMENT.PAYELEMENTTYPE AND CONVEYANCEEXEMPTIONRULE.PAYELEMENTCODE = PAYELEMENT.CODE` |
| `PAYROLLFINANCIALYEAR_FINANCIALYEAR` | `COMPANYCODE`, `FINANCIALYEARCODE` | [`PAYROLLFINANCIALYEAR`](../HR/PAYROLLFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CONVEYANCEEXEMPTIONRULE.COMPANYCODE = PAYROLLFINANCIALYEAR.COMPANYCODE AND CONVEYANCEEXEMPTIONRULE.FINANCIALYEARCODE = PAYROLLFINANCIALYEAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CONVEYANCEEXEMPTIONRULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FINANCIALYEARCODE,
       t.GROUPCODE,
       t.ITEMCODE,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.MAXAMOUNT,
       t.MAXAMOUNTDISABILITY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.CONVEYANCEEXEMPTIONRULE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
