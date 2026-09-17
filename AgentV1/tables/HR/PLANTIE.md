# DB2ADMIN.PLANTIE

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 217734

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `EMAILADDRESS` | CHAR(60) |  |  |  |  |
| 4 | `ISOCERTIFIED` | INTEGER | NOT NULL |  |  |  |
| 5 | `RANGECODE` | CHAR(15) |  |  |  |  |
| 6 | `RANGEDESCRIPTION` | CHAR(120) |  |  |  |  |
| 7 | `RANGEDIVISIONCODE` | CHAR(15) |  |  |  |  |
| 8 | `RANGEDIVISIONDESCRIPTION` | CHAR(120) |  |  |  |  |
| 9 | `COMMISIONERATE` | CHAR(30) |  |  |  |  |
| 10 | `ADDRCOMMRATE` | CHAR(100) |  |  |  |  |
| 11 | `REGISTRATIONNO` | CHAR(30) |  |  |  |  |
| 12 | `REGISTRATIONDATE` | DATE |  |  |  |  |
| 13 | `ECCNO` | CHAR(20) |  |  |  |  |
| 14 | `ECCDATE` | DATE |  |  |  |  |
| 15 | `STATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `NAMEANDDESOFEXOFF` | CHAR(100) |  |  |  |  |
| 17 | `NAMEANDDESOFEXSUP` | CHAR(100) |  |  |  |  |
| 18 | `RANGEII` | CHAR(120) |  |  |  |  |
| 19 | `PLAACCNO` | CHAR(30) |  |  |  |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PLANTIE.COMPANYCODE = COMPANY.CODE` |
| `STATE_STATE` | `STATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `PLANTIE.STATECODE = STATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PLANTIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.DIVISIONCODE,
       t.EMAILADDRESS,
       t.ISOCERTIFIED,
       t.RANGECODE,
       t.RANGEDESCRIPTION,
       t.RANGEDIVISIONCODE,
       t.RANGEDIVISIONDESCRIPTION,
       t.COMMISIONERATE,
       t.ADDRCOMMRATE,
       t.REGISTRATIONNO
FROM   DB2ADMIN.PLANTIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
