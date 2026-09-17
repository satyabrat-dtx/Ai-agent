# DB2ADMIN.SALESORDERIE

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 143980

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 5 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `TYPEOFINVOICE` | INTEGER | NOT NULL |  |  |  |
| 7 | `PCNUMBER` | CHAR(20) |  |  |  |  |
| 8 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 13 | `OURSUPPLYSTATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `SCHEMETYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `ALCODE` | CHAR(30) |  | FK | foreign_key |  |
| 16 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 17 | `ADVANCELICENSENO` | CHAR(15) |  |  |  |  |
| 18 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADVANCELICENSE_AL` | `COMPANYCODE`, `ALCODE` | [`ADVANCELICENSE`](../SALES/ADVANCELICENSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESORDERIE.COMPANYCODE = ADVANCELICENSE.COMPANYCODE AND SALESORDERIE.ALCODE = ADVANCELICENSE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SALESORDERIE.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESORDERIE.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND SALESORDERIE.COUNTERCODE = COUNTER.CODE` |
| `SCHEMETYPE_SCHEMETYPE` | `COMPANYCODE`, `SCHEMETYPECODE` | [`SCHEMETYPE`](../OTHER/SCHEMETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESORDERIE.COMPANYCODE = SCHEMETYPE.COMPANYCODE AND SALESORDERIE.SCHEMETYPECODE = SCHEMETYPE.CODE` |
| `STATE_OURSUPPLYSTATE` | `OURSUPPLYSTATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `SALESORDERIE.OURSUPPLYSTATECODE = STATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.TYPEOFINVOICE,
       t.PCNUMBER,
       t.BASICVALUE,
       t.GROSSVALUE,
       t.ROUNDOFFVALUE,
       t.NETTVALUE
FROM   DB2ADMIN.SALESORDERIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
