# DB2ADMIN.PRIMROSECUSTOMIZEDOPTIONS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 9874

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PURCHASETRANSACTIONCOUNTERCODE` | CHAR(3) |  |  |  |  |
| 2 | `SALESTRANSACTIONCOUNTERCODE` | CHAR(3) |  |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 4 | `TAXCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRIMROSECUSTOMIZEDOPTIONS.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRIMROSECUSTOMIZEDOPTIONS.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND PRIMROSECUSTOMIZEDOPTIONS.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `TAX_TAX` | `COMPANYCODE`, `TAXCODE` | [`TAX`](../CORE_MASTER/TAX.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRIMROSECUSTOMIZEDOPTIONS.COMPANYCODE = TAX.COMPANYCODE AND PRIMROSECUSTOMIZEDOPTIONS.TAXCODE = TAX.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRIMROSECUSTOMIZEDOPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PURCHASETRANSACTIONCOUNTERCODE,
       t.SALESTRANSACTIONCOUNTERCODE,
       t.ABSUNIQUEID,
       t.TAXCODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.PRIMROSECUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
